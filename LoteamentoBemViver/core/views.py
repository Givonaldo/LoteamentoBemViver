from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.views import login
from django.contrib.auth.views import logout
from django.core.urlresolvers import reverse_lazy, reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .forms import *

def home(request):
    return render(request, 'home.html')

def login_view(request, *args, **kwargs):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('core:home'))
    kwargs['extra_context'] = {'next': reverse('core:home')}
    kwargs['template_name'] = 'login.html'
    return login(request, *args, **kwargs)

def logout_view(request, *args, **kwargs):
    kwargs['next_page'] = reverse('core:home')
    return logout(request, *args, **kwargs)

class CadastroUsuarioView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('core:login')
    template_name = "register.html"

def index(request):
    template_name = 'index.html'
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('core:login'))
    return render(request, template_name)

