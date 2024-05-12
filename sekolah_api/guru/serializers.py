from rest_framework import serializers
from .models import MataPelajaran, Guru

class MataPelajaranSerializer(serializers.ModelSerializer):
    class Meta:
        model = MataPelajaran
        fields = '__all__'

class GuruSerializer(serializers.ModelSerializer):
    mata_pelajaran = MataPelajaranSerializer(many=True)

    class Meta:
        model = Guru
        fields = '__all__'
