from __future__ import unicode_literals

import datetime

from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200, default='defaultText')
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200, default='defaultText')
    votes = models.IntegerField(default=0)