from rest_framework import serializers
from .models import Kelas, Siswa

class KelasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kelas
        fields = '__all__'

class SiswaSerializer(serializers.ModelSerializer):
    kelas = KelasSerializer()

    class Meta:
        model = Siswa
        fields = '__all__'
