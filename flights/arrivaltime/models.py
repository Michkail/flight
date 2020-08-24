from django.db import models

CATEGORY = [
    ('LCTN', 'Location'),
    ('TM', 'Time')
]
class ArrivalTime(models.Model):
    class Meta:
        verbose_name = "ArrivalTime"
        verbose_name_plural = "ArrivalTime"

    name = models.CharField(max_length=50)
    category = models.CharField(choices=CATEGORY, max_length=6)

    def __str__(self):
        return self.name
