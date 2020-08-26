from rest_framework import serializers
from . import models

class OriginalURLSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.URL
        fields = ['original_url']

class NewURlSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.URL
        fields = ['new_url','validade']
    
