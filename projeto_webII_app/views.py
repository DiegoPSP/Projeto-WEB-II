from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages  # Importado para feedback do usuário
from .models import Tarefa, Inscricao  # Modelos atualizados
from .forms import FormularioTarefa     # Formulário atualizado

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


# Renomeado de listarEventos para listarTarefas
def listarTarefas(request):
    # Filtra apenas tarefas com status 'aberta'
    lista_tarefas = Tarefa.objects.filter(status='aberta').order_by('data_limite')
    
    paginator = Paginator(lista_tarefas, 5)
    num_pagina = request.GET.get('page')
    obj_pagina = paginator.get_page(num_pagina)
    
    # 🚨 ATENÇÃO: Renomeie seu template para 'app/listarTarefas.html'
    return render(request, 'app/listarTarefas.html', {'obj_pagina': obj_pagina})

# Renomeado de detalharEvento para detalharTarefa
def detalharTarefa(request, id):
    tarefa = get_object_or_404(Tarefa, pk=id)
    inscrito = False
    
    # Pega a lista de usuários inscritos
    colaboradores_inscritos = User.objects.filter(inscricoes__tarefa=tarefa)
    
    if request.user.is_authenticated:
        # Atualiza a verificação com os nomes de campos corretos
        inscrito = Inscricao.objects.filter(colaborador=request.user, tarefa=tarefa).exists()
    
    context = {
        'tarefa': tarefa,
        'inscrito': inscrito,
        'colaboradores_inscritos': colaboradores_inscritos
    }
    # 🚨 ATENÇÃO: Renomeie seu template para 'app/detalharTarefa.html'
    return render(request, 'app/detalharTarefa.html', context)

# Renomeado de criarEvento para criarTarefa
@login_required
def criarTarefa(request):
    if not request.user.is_staff:
        messages.error(request, 'Você não tem permissão para criar tarefas.')
        return redirect('listarTarefas')

    if request.method == 'POST':
        form = FormularioTarefa(request.POST, request.FILES)
        if form.is_valid():
            tarefa = form.save(commit=False)
            tarefa.criador = request.user  # Define o usuário logado como criador
            tarefa.save()
            messages.success(request, 'Tarefa criada com sucesso!')
            return redirect('listarTarefas')
    else:
        form = FormularioTarefa()
    
    # 🚨 ATENÇÃO: Renomeie seu template para 'app/formularioTarefa.html'
    return render(request, 'app/formularioTarefa.html', {'form': form, 'tipo': 'Cadastrar Tarefa'})

# Renomeado de atualizarEvento para atualizarTarefa
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
        
    # 🚨 ATENÇÃO: Renomeie seu template para 'app/formularioTarefa.html'
    return render(request, 'app/formularioTarefa.html', {'form': form, 'tipo': 'Editar Tarefa'})

# Renomeado de apagarEvento para apagarTarefa
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
    
    # 🚨 ATENÇÃO: Renomeie seu template para 'app/apagarTarefa.html'
    return render(request, 'app/apagarTarefa.html', {'objeto': tarefa, 'tipo': 'Tarefa'})


# ❌ REMOVIDAS: Todas as views de Local, Palestrante, e CategoriaEvento

# Renomeado de inscrever_evento para inscrever_tarefa
# ... (o resto das suas views e imports permanece igual)
# ...

# Renomeado de inscrever_evento para inscrever_tarefa
@login_required
def inscrever_tarefa(request, id):
    tarefa = get_object_or_404(Tarefa, pk=id)

    # Lógica de segurança: Apenas POST e apenas se a tarefa estiver aberta
    if request.method == 'POST' and tarefa.status == 'aberta':
        # get_or_create previne inscrições duplicadas
        inscricao, created = Inscricao.objects.get_or_create(
            colaborador=request.user,
            tarefa=tarefa
        )
        
        # 🚨 MUDANÇA PRINCIPAL AQUI 🚨
        # Em vez de um redirect, retornamos o template do "pedaço" de HTML.
        # O HTMX vai receber isso e atualizar a página.
        context = {'tarefa': tarefa} # Passa a tarefa, caso o partial precise
        return render(request, 'app/partials/botao_inscrito.html', context)
    
    # Se a tarefa não estiver aberta ou não for POST,
    # apenas renderiza o botão de "inscrito" (ou erro, se preferir)
    # como uma salvaguarda.
    return render(request, 'app/partials/botao_inscrito.html', {'tarefa': tarefa})


# Dashboard atualizado
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

# ... (todos os seus imports existentes)
# ... (todas as suas views existentes)

# 👇 FUNÇÃO ADICIONADA AQUI 👇

@login_required
def concluir_tarefa(request, id):
    tarefa = get_object_or_404(Tarefa, pk=id)
    
    # Segurança: Verifica se o usuário logado está inscrito na tarefa
    esta_inscrito = Inscricao.objects.filter(colaborador=request.user, tarefa=tarefa).exists()

    # Apenas quem está inscrito e está fazendo um POST pode concluir
    if request.method == 'POST' and esta_inscrito:
        # Muda o status para 'concluida'
        tarefa.status = 'concluida'
        tarefa.save()
        messages.success(request, f'Tarefa "{tarefa.titulo}" marcada como concluída!')
    
    elif not esta_inscrito:
        messages.error(request, 'Você não está inscrito nesta tarefa.')

    # Redireciona de volta para a página de detalhes
    return redirect('detalharTarefa', id=id)