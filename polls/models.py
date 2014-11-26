import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=1300)
    def __unicode__(self):
    	return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=100)
    party_description = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)
    def __unicode__(self):
    	return self.choice_text
