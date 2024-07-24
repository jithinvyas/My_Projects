from django.db import models

# Create your models here.
class Drink(models.Model):
    name = models.CharField(max_length=15)
    desc = models.CharField(max_length=30)

    def __str__(self):
        return self.name + ' ' + self.desc