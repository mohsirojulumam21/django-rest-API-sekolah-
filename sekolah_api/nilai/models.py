from django.db import models

class Nilai(models.Model):
    siswa = models.ForeignKey(Siswa, on_delete=models.CASCADE)
    mata_pelajaran = models.ForeignKey(MataPelajaran, on_delete=models.CASCADE)
    nilai = models.FloatField()
