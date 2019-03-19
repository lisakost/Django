# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

SHORT_TEXT_LEN = 700


# Create your models here.
class Articles(models.Model):
    title=models.CharField(max_length=200)
    text=models.TextField()
    user=models.ForeignKey(User)

    def get_short_text(self):
        if len(self.text) > SHORT_TEXT_LEN:
            return self.text[:SHORT_TEXT_LEN]
        else:
            return self.text


    def __str__(self):
        return self.title

