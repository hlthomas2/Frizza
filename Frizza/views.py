from django.http import HttpResponse
from django.views.generic import TemplateView
import datetime
import settings

from models import User

class LoginView(TemplateView):
    model = User
    template_name = settings.TEMPLATE_DIRS + '/public_html/login.html'
 

#    def as_view():
 #       return template_name
