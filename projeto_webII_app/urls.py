from django.urls import path, include
from . import views

urlpatterns = [
    # Rotas de Tarefas
    path('', views.listarTarefas, name='listarTarefas'),
    path('tarefas/', views.listarTarefas, name='listarTarefas_explicit'),
    path('tarefa/<int:id>/', views.detalharTarefa, name='detalharTarefa'),
    path('tarefa/novo/', views.criarTarefa, name='criarTarefa'),
    path('tarefa/<int:id>/editar/', views.atualizarTarefa, name='atualizarTarefa'),
    path('tarefa/<int:id>/apagar/', views.apagarTarefa, name='apagarTarefa'),
    path('tarefa/<int:id>/inscrever/', views.inscrever_tarefa, name='inscrever_tarefa'),
    
    # 👇 LINHA ADICIONADA AQUI 👇
    path('tarefa/<int:id>/concluir/', views.concluir_tarefa, name='concluir_tarefa'),
    
    # Rota de Dashboard
    path('dashboard/', views.admin_dashboard, name='admin_dashboard'),
    
    # Rotas de Autenticação (login, logout, etc.)
    path('', include('django.contrib.auth.urls')), 
    path('register/', views.register, name='register'),
]