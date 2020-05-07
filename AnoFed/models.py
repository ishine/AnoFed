from django.db import models

# Create your models here.
 
class Test(models.Model):
    name = models.CharField(max_length=20)

class Tokenizerdict(models.Model):
	pid = models.IntegerField(default=0)
	tokenizer = models.CharField(max_length=100)
	freq = models.IntegerField()
	pos = models.CharField(max_length=4)
