from django.db import models

class Kelas(models.Model):
    nama = models.CharField(max_length=255)

class Siswa(models.Model):
    nama = models.CharField(max_length=255)
    kelas = models.ForeignKey(Kelas, on_delete=models.CASCADE)
    alamat = models.TextField()
