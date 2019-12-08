from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView


# Create your views here.
@method_decorator(login_required, name='dispatch')
class Home(TemplateView):
    template_name = "home.html"
