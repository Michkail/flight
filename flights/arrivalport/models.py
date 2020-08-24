from django.db import models

COUNTRY = [
    ('SIN', 'Singapore'),
    ('BKK', 'Thailand'),
    ('CGK', 'Indonesia'),
    ('KUL', 'Malaysia'),
    ('MNL', 'Philippines'),
    ('SGN', 'Vietnam'),
    ('BWN', 'Brunei'),
    ('VTE', 'Laos'),
    ('RGN', 'Myanmar'),
    ('PNH', 'Kamboja')
]
class ArrivalPort(models.Model):
    class Meta:
        verbose_name = "ArrivalPort"
        verbose_name_plural = "ArrivalPort"

    name = models.CharField(max_length=50)
    country = models.CharField(choices=COUNTRY, max_length=200)

    def __str__(self):
        return self.name
