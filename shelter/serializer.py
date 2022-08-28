from rest_framework import serializers
from .models import Animal


class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('animal_id', 'animal_name', 'animal_type', 'breed',
                  'personality', 'cared_by', 'created_at', 'updated_at')
        model = Animal