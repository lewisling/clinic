from django.shortcuts import render, render_to_response, RequestContext
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect    
from django.contrib import auth                 
from django.core.context_processors import csrf 
#from .forms import RegistrationForm
from .forms import NoteForm
from two_factor.views import OTPRequiredMixin
from two_factor.views.utils import class_view_decorator
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.cache import never_cache
from django.views.generic import TemplateView, FormView



# Create your views here.
def home_page(request):
    return render(request, 'home.html')
def addpatient_page(request):
    return render(request, 'addpatient.html')   
def newnote_page(request):
    form = NoteForm(request.POST or None )
    if form.is_valid():
        save_it = form.save(commit =False)
        save_it.save()
    return render_to_response('newnote.html', locals(), context_instance = RequestContext(request))

class RegistrationView(FormView):
    template_name = 'registration.html'
    form_class = UserCreationForm
  
    def form_valid(self, form):
        form.save()
        return redirect('registration_complete')
  
  
class RegistrationCompleteView(TemplateView):
    template_name = 'registration_complete.html'
  
    def get_context_data(self, **kwargs):
        context = super(RegistrationCompleteView, self).get_context_data(**kwargs)
        context['login_url'] = str(settings.LOGIN_URL)
        return context
  



    