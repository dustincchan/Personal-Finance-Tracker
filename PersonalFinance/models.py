from django.db import models

class Bill(models.Model):
    bill_name = models.CharField(max_length=100)
    bill_cost = models.IntegerField()
    due_date = models.DateField()
