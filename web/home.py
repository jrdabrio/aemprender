from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from web.models import Alumno


# Create your views here.
@method_decorator(login_required, name='dispatch')
class Home(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        alumno = Alumno.objects.get(pk=self.request.user.pk)

        context['alumno'] = alumno
        return context
