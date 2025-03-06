from django import forms

class InsereFuncionarioForm(forms.Form):
    chefe = forms.BooleanField(
        label='Este Funcionario exerce função de Chefia?',
        required=True
    )

    biogrfia = forms.CharField(
      label='Biografia',
      required=False,
      widget=forms.Textarea  
    )

    class Meta:
        # Modelo base
        model = Funcionario

        # Campos que estarão no form
        fields = [
          'nome',
          'sobrenome',
          'cpf',
          'remuneracao'  
        ]

        # Campos que não estarão no form
        exclude = [
          'tempo_de_seervico'  
        ]


