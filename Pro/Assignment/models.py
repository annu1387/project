# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Note(models.Model):
    #msg=models.CharField(max_length=300,default="")
    msg=models.TextField()
