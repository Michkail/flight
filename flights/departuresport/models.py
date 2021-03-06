from django.db import models

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
class DeparturesPort(models.Model):
    class Meta:
        verbose_name = "DeparturesPort"
        verbose_name_plural = "DeparturesPort"

    name = models.CharField(max_length=50)
    country = models.CharField(choices=COUNTRY, max_length=200)

    def __str__(self):
        return self.name
