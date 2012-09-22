# -*- coding: utf-8 -*-
from django.db import models

from django.contrib.auth.models import User
 
class Shrt(models.Model):
    urlfull = models.TextField()
    urlmd5 = models.CharField(max_length=40,unique=True)
    urlshort = models.CharField(max_length=80)
    user = models.ForeignKey(User)
 