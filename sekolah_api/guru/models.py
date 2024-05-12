from django.db import models

class MataPelajaran(models.Model):
    nama = models.CharField(max_length=255)

class Guru(models.Model):
    nama = models.CharField(max_length=255)
    mata_pelajaran = models.ManyToManyField(MataPelajaran)
    nomor_telepon = models.CharField(max_length=20)
