from django import forms
from.models import Note
from ckeditor.widgets import CKEditorWidget
from .models import UserProfile
from django.contrib.auth.forms import UserCreationForm

class NoteForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Note
        
        
#class RegistrationForm(UserCreationForm):
#    email = forms.EmailField(required = True)
#    first_name = forms.CharField(required = False)
#    last_name = forms.CharField(required = False)
#    USER_TYPES=[('Patient','Provider'),
#         ('Patient','Provider')]
#
#    user_type = forms.ChoiceField(choices=USER_TYPES, widget=forms.RadioSelect())
#
#
#
#    class Meta:
#        model = UserProfile
#        fields = ('username', 'email', 'password1', 'password2', 'user_type')        
#
#    def save(self,commit = True):   
#        UserProfile = super(MyRegistrationForm, self).save(commit = False)
#        UserProfile.email = self.cleaned_data['email']
#        UserProfile.first_name = self.cleaned_data['first_name']
#        UserProfile.last_name = self.cleaned_data['last_name']
#        UserProfile.user_type = self.cleaned_data['user_type']
#
#
#        if commit:
#            UserProfile.save()
#
#        return UserProfile
        
class Media:
    js = ('/media/ckeditor/ckeditor.js',)
    
    
