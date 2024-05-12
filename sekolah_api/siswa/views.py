from django.shortcuts import render
from rest_framework import viewsets
from .models import Kelas, Siswa
from .serializers import KelasSerializer, SiswaSerializer
