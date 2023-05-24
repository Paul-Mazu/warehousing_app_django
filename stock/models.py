from django.db import models
from django.urls import reverse


class Item(models.Model):
    state = models.CharField(max_length=30)
    category = models.CharField(max_length=30)
    date_of_stock = models.DateTimeField()
    warehouse = models.ForeignKey("Warehouse", models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True
        db_table = "item"

    def __str__(self):
        return f"{self.state} {self.category}"

    def get_absolute_url(self):
        return reverse("model_detail", kwargs={"pk": self.pk})


class Warehouse(models.Model):
    name = models.CharField(max_length=15)

    class Meta:
        managed = True
        db_table = "warehouse"

    def __str__(self):
        return self.name
