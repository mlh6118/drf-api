from rest_framework import serializers
from .models import Animal


class AnimalSerializer(serializers.ModelSerializer):
    cared_for_by = serializers.CharField(source='cared_for_by.username')
    carer_email = serializers.CharField(source='cared_for_by.email')

    class Meta:
        fields = ('animal_id', 'animal_name', 'animal_type', 'breed',
                  'personality', 'cared_for_by', 'carer_email')
        model = Animal
