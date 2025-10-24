from django import forms
from .models import Tarefa

class FormularioTarefa(forms.ModelForm):
    class Meta:
        model = Tarefa
        
        fields = ['titulo', 'descricao', 'data_limite', 'imagem', 'projeto', 'categoria'] 
        
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'data_limite': forms.DateTimeInput(
                attrs={'type': 'datetime-local', 'class': 'form-control'},
                format='%Y-%m-%dT%H:%M'
            ),
            'imagem': forms.FileInput(attrs={'class': 'form-control'}),
            
            'projeto': forms.Select(attrs={'class': 'form-select'}),
            'categoria': forms.Select(attrs={'class': 'form-select'}),
        }
        
    def __init__(self, *args, **kwargs):
        super(FormularioTarefa, self).__init__(*args, **kwargs)
        if self.instance and self.instance.data_limite:
            self.initial['data_limite'] = self.instance.data_limite.strftime('%Y-%m-%dT%H:%M')