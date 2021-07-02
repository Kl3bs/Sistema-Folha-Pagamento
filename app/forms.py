from app.models import Funcionario
from django.forms import ModelForm

# Create the form class.
class FuncionarioForm(ModelForm):
    class Meta:
        model = Funcionario
        fields = ['nome', 'endereco', 'tipo']