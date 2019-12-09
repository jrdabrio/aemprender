from django.db import models
from django.contrib.auth.models import User


VALORES_SATISFACCION = (
    (0, "0"),
    (1, "1"),
    (2, "2"),
    (3, "3")
)


# Create your models here.
class Colegio(User):
    class Meta:
        verbose_name_plural = "Colegios"


class Alumno(User):
    school = models.ForeignKey(
        "Colegio",
        related_name="alumnos",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    class Meta:
        verbose_name_plural = "Alumnos"


class ActividadUno(models.Model):
    title = models.CharField(max_length=200, default="Titulo")
    name = models.CharField(max_length=200)
    respuesta_uno = models.CharField(max_length=200, null=True, blank=True)
    respuesta_dos = models.CharField(max_length=200, null=True, blank=True)
    respuesta_tres = models.CharField(max_length=200, null=True, blank=True)
    respuesta_cuatro = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Actividades Uno"

    def __str__(self):
        return self.name

    @property
    def get_answers(self):
        return self.respuestas.all()

    def has_previous(self):
        previous = None
        try:
            actividad = ActividadUno.objects.get(pk=self.pk - 1)
            previous = self.pk - 1
        except ActividadUno.DoesNotExist:
            previous = False
        return previous

    def has_next(self):
        next = None
        try:
            actividad = ActividadUno.objects.get(pk=self.pk + 1)
            next = self.pk + 1
        except ActividadUno.DoesNotExist:
            next = False
        return next


class RespuestasUno(models.Model):
    actividad = models.ForeignKey(
        "ActividadUno",
        on_delete=models.CASCADE,
        related_name="respuestas_uno",
    )
    alumno = models.ForeignKey(
        "Alumno",
        on_delete=models.CASCADE,
        related_name='respuestas_uno',
        blank=True,
        null=True
    )
    valor = models.IntegerField(verbose_name="Valor")

    class Meta:
        verbose_name_plural = "Respuestas Uno"

    def __str__(self):
        return self.name


class ActividadDos(models.Model):
    title = models.CharField(max_length=200, default="Titulo")
    name = models.TextField(max_length=2050)

    class Meta:
        verbose_name_plural = "Actividades Dos"

    def __str__(self):
        return self.name


class RespuestasDos(models.Model):
    actividad = models.ForeignKey(
        "ActividadDos",
        on_delete=models.CASCADE,
        related_name="respuestas_dos",
    )
    alumno = models.ForeignKey(
        "Alumno",
        on_delete=models.CASCADE,
        related_name='respuesta_dos',
        blank=True,
        null=True
    )
    valor = models.TextField(verbose_name="Respuesta", max_length=2050)

    class Meta:
        verbose_name_plural = "Respuestas Dos"

    def __str__(self):
        return self.name


class ActividadCuatro(models.Model):
    title = models.CharField(max_length=200, default="Titulo")
    name = models.TextField(max_length=2050)

    class Meta:
        verbose_name_plural = "Actividades Cuatro"

    def __str__(self):
        return self.name


class RespuestasCuatro(models.Model):
    actividad = models.ForeignKey(
        "ActividadCuatro",
        on_delete=models.CASCADE,
        related_name="respuestas_cuatro",
    )
    alumno = models.ForeignKey(
        "Alumno",
        on_delete=models.CASCADE,
        related_name='respuestas_cuatro',
        blank=True,
        null=True
    )
    valor = models.CharField(verbose_name="Respuesta", max_length=2050)

    class Meta:
        verbose_name_plural = "Respuestas Cuatro"

    def __str__(self):
        return self.name


class ActividadCinco(models.Model):
    title = models.CharField(max_length=200, default="Titulo")
    description = models.TextField(max_length=500)
    plantilla = models.Field(
        null=True,
        blank=True
    )

    class Meta:
        verbose_name_plural = "Actividades Cinco"

    def __str__(self):
        return self.title


class RespuestasCinco(models.Model):
    actividad = models.ForeignKey(
        "ActividadCinco",
        on_delete=models.CASCADE,
        related_name="respuestas_cinco",
    )
    alumno = models.ForeignKey(
        "Alumno",
        on_delete=models.CASCADE,
        related_name='respuestas_cinco',
        blank=True,
        null=True
    )
    valor = models.Field(
        null=True,
        blank=True
    )

    class Meta:
        verbose_name_plural = "Respuestas Cinco"

    def __str__(self):
        return self.name


class ActividadSeis(models.Model):
    title = models.CharField(max_length=200, default="Titulo")
    description = models.TextField(max_length=500)
    pregunta_uno = models.CharField(max_length=200, null=True, blank=True)
    pregunta_dos = models.CharField(max_length=200, null=True, blank=True)
    pregunta_tres = models.CharField(max_length=200, null=True, blank=True)
    pregunta_cuatro = models.CharField(max_length=200, null=True, blank=True)
    pregunta_cinco = models.CharField(max_length=200, null=True, blank=True)
    pregunta_seis = models.CharField(max_length=200, null=True, blank=True)
    pregunta_siete = models.CharField(max_length=200, null=True, blank=True)
    pregunta_ocho = models.CharField(max_length=200, null=True, blank=True)
    pregunta_nueve = models.CharField(max_length=200, null=True, blank=True)
    pregunta_diez = models.CharField(max_length=200, null=True, blank=True)
    pregunta_once = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Actividades Seis"

    def __str__(self):
        return self.title


class RespuestasSeis(models.Model):
    actividad = models.ForeignKey(
        "ActividadSeis",
        on_delete=models.CASCADE,
        related_name="respuestas_seis",
    )
    alumno = models.ForeignKey(
        "Alumno",
        on_delete=models.CASCADE,
        related_name='respuestas_seis',
        blank=True,
        null=True
    )
    respuesta_uno = models.IntegerField(null=True, blank=True, choices=VALORES_SATISFACCION)
    respuesta_dos = models.IntegerField(null=True, blank=True, choices=VALORES_SATISFACCION)
    respuesta_tres = models.IntegerField(null=True, blank=True, choices=VALORES_SATISFACCION)
    respuesta_cuatro = models.IntegerField(null=True, blank=True, choices=VALORES_SATISFACCION)
    respuesta_cinco = models.IntegerField(null=True, blank=True, choices=VALORES_SATISFACCION)
    respuesta_seis = models.IntegerField(null=True, blank=True, choices=VALORES_SATISFACCION)
    respuesta_siete = models.IntegerField(null=True, blank=True, choices=VALORES_SATISFACCION)
    respuesta_ocho = models.IntegerField(null=True, blank=True, choices=VALORES_SATISFACCION)
    respuesta_nueve = models.IntegerField(null=True, blank=True, choices=VALORES_SATISFACCION)
    respuesta_diez = models.IntegerField(null=True, blank=True, choices=VALORES_SATISFACCION)
    respuesta_once = models.IntegerField(null=True, blank=True, choices=VALORES_SATISFACCION)

    class Meta:
        verbose_name_plural = "Respuestas Seis"

    def __str__(self):
        return self.name
