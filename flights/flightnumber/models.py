from django.db import models

CATEGORY = [
    ('C', 'Code'),
    ('B', 'Boeing')
]
class FlightsNumber(models.Model):
    class Meta:
        verbose_name = "FlightsNumber"
        verbose_name_plural = "FlightsNumber"

    name = models.CharField(max_length=50)
    category = models.CharField(choices=CATEGORY, max_length=6)

    def __str__(self):
        return self.name
