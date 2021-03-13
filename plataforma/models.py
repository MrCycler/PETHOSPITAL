from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Client (models.Model):
    name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30, blank=False)
    address = models.CharField(max_length=100, blank=True)
    ocupation = models.CharField(max_length=30, blank=True)
    # dni
    dni_regex = RegexValidator(regex=r'^[0-9]{8}$', message="El número de DNI debe tener un formato válido.")
    dni = models.CharField(validators=[dni_regex],max_length=8, blank=False, unique=True)
    # telefono
    phone_regex = RegexValidator(regex=r'^[0-9]{9}$', message="El número telefonico debe tener un formato válido.")
    phone = models.CharField(validators=[phone_regex],max_length=9, blank=False)
    # email
    email_regex = RegexValidator(regex=r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', message="El correo electrónico debe tener un formato válido.")
    e_mail = models.EmailField(validators=[email_regex],max_length = 254, blank=False,unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

TYPES = [('DOG','DOG'),('CAT','CAT'),('PARROT','PARROT')]

class Pet (models.Model):
    pet_type = models.CharField(max_length=30,choices=TYPES, blank=False)
    race = models.CharField(max_length=30, blank=True)
    name = models.CharField(max_length=30, blank=False)
    age = models.PositiveIntegerField(blank=False)
    birthday = models.DateField(blank=False)
    #*image
    image = models.ImageField(upload_to='pets/%Y/%m/%d/',blank=True)
    # one to many 
    client = models.ForeignKey(Client,verbose_name='client', on_delete=models.CASCADE, blank=False) #models.ManyToManyField #models.OneToOneField
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

class Doctor (models.Model):
    name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30, blank=False)
    address = models.CharField(max_length=100, blank=True)
    # dni
    dni_regex = RegexValidator(regex=r'^[0-9]{8}$', message="El número de DNI debe tener un formato válido.")
    dni = models.CharField(validators=[dni_regex],max_length=8, blank=False, unique=True)
    # telefono
    phone_regex = RegexValidator(regex=r'^[0-9]{9}$', message="El número telefonico debe tener un formato válido.")
    phone = models.CharField(validators=[phone_regex],max_length=9, blank=False)
    # email
    email_regex = RegexValidator(regex=r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', message="El correo electrónico debe tener un formato válido.")
    e_mail = models.EmailField(validators=[email_regex],max_length = 254, blank=False,unique=True)
    salary = models.PositiveIntegerField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)