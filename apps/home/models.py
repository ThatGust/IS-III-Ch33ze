# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

class Estudiante(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Otros campos de Estudiante

class Profesor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Otros campos de Profesor

