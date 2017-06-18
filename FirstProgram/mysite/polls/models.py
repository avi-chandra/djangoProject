# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    @property
    def __str__(self):
        return self.question_text


class Choice(models.Model):
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.choice_text

class Person_details(models.Model):
    fullName = models.CharField(max_length=40)
    idcardNum = models.CharField(max_length=15, unique=True)
    age = models.IntegerField()
    education = models.CharField(max_length=20)
    city = models.CharField(max_length=35)
    state = models.CharField(max_length=35)
    added_date = models.DateTimeField('date when added')

class States(models.Model):
    state = models.CharField(max_length=50)
    ad_date = models.DateTimeField('date when added')

    def __str__(self):
        return self.state

class Cities(models.Model):
    cities = models.CharField(max_length=45)
    state_id = models.ForeignKey(States, on_delete=models.CASCADE)

    def __str__(self):
        return self.cities