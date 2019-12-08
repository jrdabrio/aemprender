from django import forms

from .models import (
    RespuestasUno,
    RespuestasDos,
    RespuestasCuatro,
    RespuestasCinco,
    RespuestasSeis
)


class RespuestasUnoForm(forms.ModelForm):

    class Meta:
        model = RespuestasUno
        fields = ['valor']


class RespuestasDosForm(forms.ModelForm):

    class Meta:
        model = RespuestasDos
        fields = ['valor']
        widgets = {
            'valor': forms.Textarea(attrs={'placeholder': u'Escribe aquí tu respuesta.', 'rows': 8, 'cols': 15}),
        }


class RespuestasCuatroForm(forms.ModelForm):

    class Meta:
        model = RespuestasCuatro
        fields = ['valor']
        widgets = {
            'valor': forms.Textarea(attrs={'placeholder': u'Escribe aquí tu propuesta.', 'rows': 50, 'cols': 15}),
        }


class RespuestasCincoForm(forms.ModelForm):

    class Meta:
        model = RespuestasCinco
        fields = ['valor']


class RespuestasSeisForm(forms.ModelForm):

    class Meta:
        model = RespuestasSeis
        exclude = ['alumno', 'actividad']
