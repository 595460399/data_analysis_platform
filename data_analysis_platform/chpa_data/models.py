from django.db import models


# Create your models here.

class TestData(models.Model):
    tc_1 = models.CharField(max_length=100)
    tc_2 = models.CharField(max_length=100)
    tc_3 = models.CharField(max_length=100)
    tc_4 = models.CharField(max_length=100)
    molecule = models.CharField(max_length=100)
    product = models.CharField(max_length=100)
    package = models.CharField(max_length=100)
    corporation = models.CharField(max_length=100)
    manuf_type = models.CharField(max_length=100)
    formulation = models.CharField(max_length=100)
    strength = models.CharField(max_length=100)
    amount = models.FloatField()
    unit = models.CharField(max_length=100)
    period = models.CharField(max_length=100)
    date_time = models.DateField()

    class Meta:
        db_table = 'test_data'
