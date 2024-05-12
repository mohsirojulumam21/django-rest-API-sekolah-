from rest_framework import serializers
from .models import Nilai
from siswa.serializers import SiswaSerializer
from guru.serializers import MataPelajaranSerializer

class NilaiSerializer(serializers.ModelSerializer):
    siswa = SiswaSerializer()
    mata_pelajaran = MataPelajaranSerializer()

    class Meta:
        model = Nilai
        fields = '__all__'
