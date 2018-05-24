from django.db import models

# Create your models here.

class Msg(models.Model):
    msg_text = models.CharField(max_length=200)
    msg_sender = models.CharField(max_length=64)
    pub_date = models.DateTimeField('date published')
    