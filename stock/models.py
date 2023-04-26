from django.db import models
from django.urls import reverse


class Employee(models.Model):
    user_name = models.CharField(primary_key=True, max_length=20)
    password = models.TextField()
    lead_by = models.ForeignKey(
        'self', models.DO_NOTHING, db_column='lead_by', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employee'


class Item(models.Model):
    state = models.CharField(max_length=30)
    category = models.CharField(max_length=30)
    date_of_stock = models.DateTimeField()
    warehouse = models.ForeignKey(
        'Warehouse', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'item'

    def __str__(self):
        return f"{self.state} {self.category}"
    
    def get_absolute_url(self):
        return reverse("model_detail", kwargs={"pk": self.pk})
    


class Warehouse(models.Model):
    name = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'warehouse'
