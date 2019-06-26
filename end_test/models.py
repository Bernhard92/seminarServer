from django.db import models

# Create your models here.
class TestParticipant(models.Model):
	firstname = models.CharField(max_length=200)
	lastname = models.CharField(max_length=200)
	test_date = models.DateTimeField()
	answers = models.CharField(max_length=200)
	result = models.DecimalField(max_digits=4, decimal_places=2) 
