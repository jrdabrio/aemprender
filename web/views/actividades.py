from django.urls import reverse_lazy
from django.views.generic import FormView
from django.contrib import messages

from web.models import (
    ActividadUno,
    RespuestasUno,
    ActividadDos,
    RespuestasDos,
    ActividadTres,
    RespuestasTres,
    ActividadCuatro,
    RespuestasCuatro,
    ActividadCinco,
    RespuestasCinco,
    ActividadSeis,
    RespuestasSeis,
    Alumno
)
from web.forms import (
    RespuestasUnoForm,
    RespuestasDosForm,
    RespuestasTresForm,
    RespuestasCuatroForm,
    RespuestasCincoForm,
    RespuestasSeisForm
)


class ActividadUnoView(FormView):
    template_name = "actividades/actividad-uno.html"
    form_class = RespuestasUnoForm
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['actividades'] = ActividadUno.objects.all()
        actividad = ActividadUno.objects.get(pk=int(self.kwargs.get('pk')))
        context['actividad_actual'] = actividad
        context['menu_actual'] = 1
        return context

    def get_success_url(self):
        actividad = ActividadUno.objects.get(pk=int(self.kwargs.get('pk')))
        next = actividad.has_next()
        if next:
            return reverse_lazy('actividad-uno', kwargs={'pk': next})
        return reverse_lazy('home')

    def get_initial(self):
        """
        Returns the initial data to use for forms on this view.
        """
        actividad = ActividadUno.objects.get(pk=int(self.kwargs.get('pk')))
        alumno = Alumno.objects.get(pk=self.request.user.pk)
        initial = super(ActividadUnoView, self).get_initial()

        try:
            respuesta = RespuestasUno.objects.get(actividad=actividad, alumno=alumno)
            initial['valor'] = respuesta.valor
        except RespuestasUno.DoesNotExist:
            initial = []

        return initial

    def form_valid(self, form):
        actividad = ActividadUno.objects.get(pk=int(self.kwargs.get('pk')))
        alumno = Alumno.objects.get(pk=self.request.user.pk)
        cleaned_data = form.cleaned_data
        try:
            respuesta = RespuestasUno.objects.get(actividad=actividad, alumno=alumno)
            respuesta.valor = cleaned_data.get('valor')
            respuesta.save()
        except RespuestasUno.DoesNotExist:
            respuesta = RespuestasUno.objects.get_or_create(
                actividad=actividad,
                alumno=alumno,
                valor=cleaned_data.get('valor')
            )
        if not actividad.has_next():
            messages.success(self.request, '¡Actividad uno completada!.')

        return super().form_valid(form)


class ActividadDosView(FormView):
    template_name = "actividades/actividad-dos.html"
    form_class = RespuestasDosForm
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['actividad_actual'] = ActividadDos.objects.first()
        context['menu_actual'] = 2
        return context

    def get_initial(self):
        """
        Returns the initial data to use for forms on this view.
        """
        actividad = ActividadDos.objects.first()
        alumno = Alumno.objects.get(pk=self.request.user.pk)
        initial = super(ActividadDosView, self).get_initial()

        try:
            respuesta = RespuestasDos.objects.get(actividad=actividad, alumno=alumno)
            initial['valor'] = respuesta.valor
        except RespuestasDos.DoesNotExist:
            initial = []

        return initial

    def form_valid(self, form):
        actividad = ActividadDos.objects.first()
        alumno = Alumno.objects.get(pk=self.request.user.pk)
        cleaned_data = form.cleaned_data
        try:
            respuesta = RespuestasDos.objects.get(actividad=actividad, alumno=alumno)
            respuesta.valor = cleaned_data.get('valor')
            respuesta.save()
        except RespuestasDos.DoesNotExist:
            respuesta = RespuestasDos.objects.get_or_create(
                actividad=actividad,
                alumno=alumno,
                valor=cleaned_data.get('valor')
            )

        messages.success(self.request, '¡Actividad dos completada!.')

        return super().form_valid(form)


class ActividadTresView(FormView):
    template_name = "actividades/actividad-tres.html"
    form_class = RespuestasTresForm
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['actividad_actual'] = ActividadTres.objects.first()
        context['menu_actual'] = 3
        return context

    def get_initial(self):
        """
        Returns the initial data to use for forms on this view.
        """
        actividad = ActividadTres.objects.first()
        alumno = Alumno.objects.get(pk=self.request.user.pk)
        initial = super(ActividadTresView, self).get_initial()

        try:
            respuesta = RespuestasTres.objects.get(actividad=actividad, alumno=alumno)
            initial['valor'] = respuesta.valor
        except RespuestasTres.DoesNotExist:
            initial = []

        return initial

    def form_valid(self, form):
        actividad = ActividadTres.objects.first()
        alumno = Alumno.objects.get(pk=self.request.user.pk)
        cleaned_data = form.cleaned_data
        try:
            respuesta = RespuestasTres.objects.get(actividad=actividad, alumno=alumno)
            respuesta.valor = cleaned_data.get('valor')
            respuesta.save()
        except RespuestasTres.DoesNotExist:
            respuesta = RespuestasTres.objects.get_or_create(
                actividad=actividad,
                alumno=alumno,
                valor=cleaned_data.get('valor')
            )

        messages.success(self.request, '¡Actividad tres completada!.')

        return super().form_valid(form)


class ActividadCuatroView(FormView):
    template_name = "actividades/actividad-cuatro.html"
    form_class = RespuestasCuatroForm
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['actividad_actual'] = ActividadCuatro.objects.first()
        context['menu_actual'] = 4
        return context

    def get_initial(self):
        """
        Returns the initial data to use for forms on this view.
        """
        actividad = ActividadCuatro.objects.first()
        alumno = Alumno.objects.get(pk=self.request.user.pk)
        initial = super(ActividadCuatroView, self).get_initial()

        try:
            respuesta = RespuestasCuatro.objects.get(actividad=actividad, alumno=alumno)
            initial['valor'] = respuesta.valor
        except RespuestasCuatro.DoesNotExist:
            initial = []

        return initial

    def form_valid(self, form):
        actividad = ActividadCuatro.objects.first()
        alumno = Alumno.objects.get(pk=self.request.user.pk)
        cleaned_data = form.cleaned_data
        try:
            respuesta = RespuestasCuatro.objects.get(actividad=actividad, alumno=alumno)
            respuesta.valor = cleaned_data.get('valor')
            respuesta.save()
        except RespuestasCuatro.DoesNotExist:
            respuesta = RespuestasCuatro.objects.get_or_create(
                actividad=actividad,
                alumno=alumno,
                valor=cleaned_data.get('valor')
            )

        messages.success(self.request, '¡Actividad cuatro completada!.')

        return super().form_valid(form)


class ActividadCincoView(FormView):
    template_name = "actividades/actividad-cinco.html"
    form_class = RespuestasCincoForm
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['actividad_actual'] = ActividadCinco.objects.first()
        context['menu_actual'] = 5
        return context

    def get_initial(self):
        """
        Returns the initial data to use for forms on this view.
        """
        actividad = ActividadCinco.objects.first()
        alumno = Alumno.objects.get(pk=self.request.user.pk)
        initial = super(ActividadCincoView, self).get_initial()

        try:
            respuesta = RespuestasCinco.objects.get(actividad=actividad, alumno=alumno)
            initial['valor'] = respuesta.valor
        except RespuestasCinco.DoesNotExist:
            initial = []

        return initial

    def form_valid(self, form):
        actividad = ActividadCinco.objects.first()
        alumno = Alumno.objects.get(pk=self.request.user.pk)
        cleaned_data = form.cleaned_data
        try:
            respuesta = RespuestasCinco.objects.get(actividad=actividad, alumno=alumno)
            respuesta.valor = cleaned_data.get('valor')
            respuesta.save()
        except RespuestasCinco.DoesNotExist:
            respuesta = RespuestasCinco.objects.get_or_create(
                actividad=actividad,
                alumno=alumno,
                valor=cleaned_data.get('valor')
            )

        messages.success(self.request, '¡Actividad cinco completada!.')

        return super().form_valid(form)


class ActividadSeisView(FormView):
    template_name = "actividades/actividad-seis.html"
    form_class = RespuestasSeisForm
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['actividad_actual'] = ActividadSeis.objects.first()
        context['menu_actual'] = 6
        return context

    def get_initial(self):
        """
        Returns the initial data to use for forms on this view.
        """
        actividad = ActividadSeis.objects.first()
        alumno = Alumno.objects.get(pk=self.request.user.pk)
        initial = super(ActividadSeisView, self).get_initial()

        try:
            respuesta = RespuestasSeis.objects.get(actividad=actividad, alumno=alumno)
            initial['respuesta_uno'] = respuesta.respuesta_uno
            initial['respuesta_dos'] = respuesta.respuesta_dos
            initial['respuesta_tres'] = respuesta.respuesta_tres
            initial['respuesta_cuatro'] = respuesta.respuesta_cuatro
            initial['respuesta_cinco'] = respuesta.respuesta_cinco
            initial['respuesta_seis'] = respuesta.respuesta_seis
            initial['respuesta_siete'] = respuesta.respuesta_siete
            initial['respuesta_ocho'] = respuesta.respuesta_ocho
            initial['respuesta_nueve'] = respuesta.respuesta_nueve
            initial['respuesta_diez'] = respuesta.respuesta_diez
            initial['respuesta_once'] = respuesta.respuesta_once
        except RespuestasSeis.DoesNotExist:
            initial = []

        return initial

    def form_valid(self, form):
        actividad = ActividadSeis.objects.first()
        alumno = Alumno.objects.get(pk=self.request.user.pk)
        cleaned_data = form.cleaned_data
        try:
            respuesta = RespuestasSeis.objects.get(actividad=actividad, alumno=alumno)
            respuesta.respuesta_uno = cleaned_data.get('respuesta_uno')
            respuesta.respuesta_dos = cleaned_data.get('respuesta_dos')
            respuesta.respuesta_tres = cleaned_data.get('respuesta_tres')
            respuesta.respuesta_cuatro = cleaned_data.get('respuesta_cuatro')
            respuesta.respuesta_cinco = cleaned_data.get('respuesta_cinco')
            respuesta.respuesta_seis = cleaned_data.get('respuesta_seis')
            respuesta.respuesta_siete = cleaned_data.get('respuesta_siete')
            respuesta.respuesta_ocho = cleaned_data.get('respuesta_ocho')
            respuesta.respuesta_nueve = cleaned_data.get('respuesta_nueve')
            respuesta.respuesta_diez = cleaned_data.get('respuesta_diez')
            respuesta.respuesta_once = cleaned_data.get('respuesta_once')
            respuesta.save()
        except RespuestasSeis.DoesNotExist:
            respuesta = RespuestasSeis.objects.get_or_create(
                actividad=actividad,
                alumno=alumno,
                respuesta_uno=cleaned_data.get('respuesta_uno'),
                respuesta_dos=cleaned_data.get('respuesta_dos'),
                respuesta_tres=cleaned_data.get('respuesta_tres'),
                respuesta_cuatro=cleaned_data.get('respuesta_cuatro'),
                respuesta_cinco=cleaned_data.get('respuesta_cinco'),
                respuesta_seis=cleaned_data.get('respuesta_seis'),
                respuesta_siete=cleaned_data.get('respuesta_siete'),
                respuesta_ocho=cleaned_data.get('respuesta_ocho'),
                respuesta_nueve=cleaned_data.get('respuesta_nueve'),
                respuesta_diez=cleaned_data.get('respuesta_diez'),
                respuesta_once=cleaned_data.get('respuesta_once')
            )

        messages.success(self.request, '¡Actividad seis completada!.')

        return super().form_valid(form)

    def form_invalid(self, form):
        ok = True
        return super().form_invalid(form)
