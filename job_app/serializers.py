from rest_framework import serializers
from .models import Job

class JobSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Job
        fields = '__all__'
