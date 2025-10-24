from django.db import models
from django.contrib.auth.models import User

class Projeto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    criador = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='projetos_criados')

    class Meta:
        verbose_name = "Projeto"
        verbose_name_plural = "Projetos"
        ordering = ['nome']

    def __str__(self):
        return self.nome

class Categoria(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    
    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering = ['nome']

    def __str__(self):
        return self.nome

class Tarefa(models.Model):
    STATUS_CHOICES = [
        ('aberta', 'Aberta para Inscrição'),
        ('em_andamento', 'Em Andamento'),
        ('concluida', 'Concluída'),
    ]

    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    data_limite = models.DateTimeField(verbose_name="Data Limite")
    criador = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='tarefas_criadas')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='aberta')
    imagem = models.ImageField(upload_to='tarefas/', blank=True, null=True, verbose_name="Imagem da Tarefa")
    
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE, related_name='tarefas', null=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True, related_name='tarefas')

    class Meta:
        verbose_name = "Tarefa"
        verbose_name_plural = "Tarefas"
        ordering = ['data_limite']

    def __str__(self):
        return self.titulo

class Inscricao(models.Model):
    colaborador = models.ForeignKey(User, on_delete=models.CASCADE, related_name='inscricoes')
    tarefa = models.ForeignKey(Tarefa, on_delete=models.CASCADE, related_name='inscricoes')
    data_inscricao = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('colaborador', 'tarefa')
        verbose_name = "Inscrição"
        verbose_name_plural = "Inscrições"

    def __str__(self):
        return f'{self.colaborador.username} inscrito em {self.tarefa.titulo}'


class Comentario(models.Model):
    tarefa = models.ForeignKey(Tarefa, on_delete=models.CASCADE, related_name='comentarios')
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comentarios')
    texto = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Comentário"
        verbose_name_plural = "Comentários"
        ordering = ['data_criacao'] 

    def __str__(self):
        return f'Comentário de {self.autor.username} em {self.tarefa.titulo}'