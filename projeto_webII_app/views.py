from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages  
from .models import Tarefa, Inscricao 
from .forms import FormularioTarefa    

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Conta criada com sucesso! Por favor, faça o login.')
            return redirect('login')
        else:
            messages.error(request, 'Houve um erro no registro. Verifique os dados.')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


def listarTarefas(request):
    lista_tarefas = Tarefa.objects.filter(status='aberta').order_by('data_limite')
    
    paginator = Paginator(lista_tarefas, 5)
    num_pagina = request.GET.get('page')
    obj_pagina = paginator.get_page(num_pagina)
    
    return render(request, 'app/listarTarefas.html', {'obj_pagina': obj_pagina})

def detalharTarefa(request, id):
    tarefa = get_object_or_404(Tarefa, pk=id)
    inscrito = False
    
    colaboradores_inscritos = User.objects.filter(inscricoes__tarefa=tarefa)
    
    if request.user.is_authenticated:
        inscrito = Inscricao.objects.filter(colaborador=request.user, tarefa=tarefa).exists()
    
    context = {
        'tarefa': tarefa,
        'inscrito': inscrito,
        'colaboradores_inscritos': colaboradores_inscritos
    }
    return render(request, 'app/detalharTarefa.html', context)

@login_required
def criarTarefa(request):
    if not request.user.is_staff:
        messages.error(request, 'Você não tem permissão para criar tarefas.')
        return redirect('listarTarefas')

    if request.method == 'POST':
        form = FormularioTarefa(request.POST, request.FILES)
        if form.is_valid():
            tarefa = form.save(commit=False)
            tarefa.criador = request.user  
            tarefa.save()
            messages.success(request, 'Tarefa criada com sucesso!')
            return redirect('listarTarefas')
    else:
        form = FormularioTarefa()
    
    return render(request, 'app/formularioTarefa.html', {'form': form, 'tipo': 'Cadastrar Tarefa'})

@login_required
def atualizarTarefa(request, id):
    if not request.user.is_staff:
        messages.error(request, 'Você não tem permissão para editar tarefas.')
        return redirect('listarTarefas')

    tarefa = get_object_or_404(Tarefa, pk=id)
    form = FormularioTarefa(request.POST or None, request.FILES or None, instance=tarefa)
    
    if form.is_valid():
        form.save()
        messages.success(request, 'Tarefa atualizada com sucesso.')
        return redirect('listarTarefas')
        
    return render(request, 'app/formularioTarefa.html', {'form': form, 'tipo': 'Editar Tarefa'})

@login_required
def apagarTarefa(request, id):
    if not request.user.is_staff:
        messages.error(request, 'Você não tem permissão para apagar tarefas.')
        return redirect('listarTarefas')
    
    tarefa = get_object_or_404(Tarefa, pk=id)
    if request.method == 'POST':
        tarefa.delete()
        messages.success(request, 'Tarefa apagada com sucesso.')
        return redirect('listarTarefas')
    
    return render(request, 'app/apagarTarefa.html', {'objeto': tarefa, 'tipo': 'Tarefa'})

@login_required
def inscrever_tarefa(request, id):
    tarefa = get_object_or_404(Tarefa, pk=id)

    if request.method == 'POST' and tarefa.status == 'aberta':
        inscricao, created = Inscricao.objects.get_or_create(
            colaborador=request.user,
            tarefa=tarefa
        )
        context = {'tarefa': tarefa} 
        return render(request, 'app/partials/botao_inscrito.html', context)

    return render(request, 'app/partials/botao_inscrito.html', {'tarefa': tarefa})


@login_required
def admin_dashboard(request):
    if not request.user.is_staff:
        return redirect('listarTarefas')

    num_tarefas = Tarefa.objects.count()
    num_usuarios = User.objects.count()
    num_inscricoes = Inscricao.objects.count()
    num_tarefas_abertas = Tarefa.objects.filter(status='aberta').count()

    context = {
        'num_tarefas': num_tarefas,
        'num_usuarios': num_usuarios,
        'num_inscricoes': num_inscricoes,
        'num_tarefas_abertas': num_tarefas_abertas,
    }
    
    return render(request, 'app/admin_dashboard.html', context)

@login_required
def concluir_tarefa(request, id):
    tarefa = get_object_or_404(Tarefa, pk=id)
    
    esta_inscrito = Inscricao.objects.filter(colaborador=request.user, tarefa=tarefa).exists()

    if request.method == 'POST' and esta_inscrito:
        tarefa.status = 'concluida'
        tarefa.save()
        messages.success(request, f'Tarefa "{tarefa.titulo}" marcada como concluída!')
    
    elif not esta_inscrito:
        messages.error(request, 'Você não está inscrito nesta tarefa.')

    return redirect('detalharTarefa', id=id)


@login_required
def listarTodosUsuariosView(request):
    if not request.user.is_staff:
        messages.error(request, 'Acesso não autorizado.')
        return redirect('listarTarefas')

    lista_usuarios = User.objects.all().order_by('username')
    context = {
        'lista_usuarios': lista_usuarios,
    }
    return render(request, 'app/listarUsuarios.html', context) 

@login_required
def listarTodasTarefasView(request):

    if not request.user.is_staff:
        messages.error(request, 'Acesso não autorizado.')
        return redirect('listarTarefas')

    lista_tarefas = Tarefa.objects.all().order_by('-data_limite')
    
    paginator = Paginator(lista_tarefas, 10)
    num_pagina = request.GET.get('page')
    obj_pagina = paginator.get_page(num_pagina)
    
    context = {
        'obj_pagina': obj_pagina,
        'titulo_pagina': 'Todas as Tarefas Cadastradas'
    }
    
    return render(request, 'app/listarTarefas.html', context)