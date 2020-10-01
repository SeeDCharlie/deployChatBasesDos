from chat.models import *
from rest_framework import serializers

class szc_states(serializers.ModelSerializer):
    
    class Meta:
        model = c_states
        fields = '__all__'

class sz_users(serializers.ModelSerializer):

    class Meta:
        model = users
        fields = ['id','username','email']
