import re
from django.db import models


class Applicant(models.Model):
    name = models.CharField(max_length=100)
    birth = models.DateField()
    telephone = models.IntegerField()
    health = models.CharField(max_length=100)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.concept


class Appeal(models.Model):
    application = models.ForeignKey(Applicant, on_delete=models.CASCADE, related_name='application')
    date = models.DateField()
    number = models.IntegerField()

    class Meta:
        ordering = ('date', 'number')

    def __str__(self):
        return self.concept


class Emergency(models.Model):
    appeal = models.ForeignKey(Appeal, on_delete=models.CASCADE, related_name='appeal')
    name = models.CharField(max_length=30)
    code = models.IntegerField()
    telephone = models.IntegerField() 

    class Meta:
        ordering = ('code',)

    def __str__(self):
        return self.concept
