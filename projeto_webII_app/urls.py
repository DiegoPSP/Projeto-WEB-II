from django.urls import path, include
from . import views

urlpatterns = [

    path('', views.listarTarefas, name='listarTarefas'),
    path('tarefas/', views.listarTarefas, name='listarTarefas_explicit'),
    
 
    path('tarefa/<int:id>/', views.detalharTarefa, name='detalharTarefa'),
    path('tarefa/novo/', views.criarTarefa, name='criarTarefa'),
    path('tarefa/<int:id>/editar/', views.atualizarTarefa, name='atualizarTarefa'),
    path('tarefa/<int:id>/apagar/', views.apagarTarefa, name='apagarTarefa'),

    path('tarefa/<int:id>/inscrever/', views.inscrever_tarefa, name='inscrever_tarefa'),
    path('tarefa/<int:id>/concluir/', views.concluir_tarefa, name='concluir_tarefa'),
    

    path('dashboard/', views.admin_dashboard, name='admin_dashboard'),
   
    path('dashboard/usuarios/', views.listarTodosUsuariosView, name='listar_usuarios'),
    path('dashboard/tarefas-todas/', views.listarTodasTarefasView, name='listar_tarefas_todas'),
    
    path('', include('django.contrib.auth.urls')), 
    path('register/', views.register, name='register'),
]

