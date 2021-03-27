# *Importa los serializers base
from rest_framework import serializers
from .models import Client, Pet, Doctor

class ClientSerializer (serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id','name','last_name','address','ocupation','dni','phone','e_mail','created_at','modified_at']
        read_only_fields = ['id','created_at','modified_at']


