from django.shortcuts import render, render_to_response, RequestContext
from django.shortcuts import render
from django.http import HttpResponseRedirect    
from django.contrib import auth                 
from django.core.context_processors import csrf 
#from .forms import RegistrationForm
from .forms import NoteForm

# Create your views here.
def home_page(request):
    return render(request, 'home.html')
def register_user(request):
    return render(request, 'register.html')
def newnote_page(request):
    form = NoteForm(request.POST or None )
    if form.is_valid():
        save_it = form.save(commit =False)
        save_it.save()
    return render_to_response('newnote.html', locals(), context_instance = RequestContext(request))



def addpatient_page(request):
    return render(request, 'addpatient.html')   
    