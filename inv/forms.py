from django import forms

from .models import Categoria

class CategoriaForm(forms.ModelForm):
    class Meta:
        model =  Categoria
        fields = ['descripcion','esatdo']
        labels = {'descripcion':'Descripcion de la Categoria',
                    'estado':'Estado'}
        widget = {'descripcion':forms.TextInput}

    def __init__(self,*args, **Kwargs):
        super().__init__(*args, **Kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })