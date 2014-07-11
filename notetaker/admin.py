from django import forms
from django.contrib import admin
from ckeditor.widgets import CKEditorWidget

from .models import Note

class NoteAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Note

class NoteAdmin(admin.ModelAdmin):
    form = NoteAdminForm

admin.site.register(Note, NoteAdmin)