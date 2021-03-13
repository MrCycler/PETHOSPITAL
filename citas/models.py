from django.db import models
from plataforma.models import Pet, Doctor
from django.contrib.auth.models import User

# Create your models here.
class Appointment (models.Model):
    # one to many 
    pet = models.ForeignKey(Pet,verbose_name='pet', on_delete=models.CASCADE, blank=False) 
    # one to many 
    doctor = models.ForeignKey(Doctor,verbose_name='doctor', on_delete=models.CASCADE, blank=False)
    appointment_date = models.DateField(blank=False)
    duration_hours = models.PositiveIntegerField(blank=False)
    # one to many 
    creator = models.ForeignKey(User,verbose_name='creator', on_delete=models.CASCADE, blank=True) #TODO: revisar si es conveniente el on_delete?
    is_completed = models.BooleanField(blank=False,default=False)
    reason = models.CharField(max_length=200, blank=True)
    recipe = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)