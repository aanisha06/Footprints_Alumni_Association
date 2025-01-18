from rest_framework import serializers
from .models import OfficialAlumni

class AlumniSerializer(serializers.ModelSerializer):
    class Meta:
        model = OfficialAlumni
        fields =['regno','studentname','mobile','batchid']
# 22352001