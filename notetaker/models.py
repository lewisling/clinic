from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import smart_unicode
from ckeditor.fields import RichTextField

class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    USER_TYPES = (
        ('P', 'PATIENT'),
        ('R', 'PROVIDER'),
    )
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    user_type = models.CharField(max_length=1, choices=USER_TYPES)
    
class Note(models.Model):
    title=models.CharField(max_length=120, null=True, blank=True)
    text = RichTextField()
    date = models.DateTimeField()
    #created_timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    
    def __unicode__(self):
        return smart_unicode(self.title)
        
class Patient(models.Model):
    patient_name = models.ForeignKey(UserProfile)
    note_name = models.ForeignKey(Note)
    adrs = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    zip = models.CharField(max_length=5)
    
class Provider(models.Model):
    SPECIALITY_TYPES = (
        ('1', 'DERMATOLOGY'),
        ('2', 'ANESTHESIOLOGY'),
        ('3', 'PHYSICAL MEDICINE AND REHABILITATION'),
        ('4', 'FAMILY MEDICINE'),
        ('5', 'INTERNAL MEDICINE'),
        ('6', 'GYNECOLOGY'),
        ('7', 'PEDIATRICS'),
        ('8', 'OPHTHALMOLOGY'),
        ('9', 'RADIOLOGY'),
    )
    provider_name = models.ForeignKey(UserProfile)
    speciality = models.CharField(max_length=1, choices=SPECIALITY_TYPES)
    provider_code = models.IntegerField()
    
    
