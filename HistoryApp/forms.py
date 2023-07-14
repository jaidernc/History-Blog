from django import forms

class TemaFormulario(forms.Form):
    tema = forms.CharField()
    categoria = forms.CharField()

class AdminFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
    cargo = forms.CharField()

class UsuarioFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
    edad = forms.IntegerField()