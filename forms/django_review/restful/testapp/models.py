from django.db import models

# Create your models here.
class TesterModel(models.Model):
    name = models.CharField(max_length=50)
    element = models.CharField(max_length = 3)
    level = models.IntegerField(default=1)

    def __str__(self):
        return self.name