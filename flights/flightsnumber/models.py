from django.db import models

from django.db import models

NUMBER = [
    ('A', 'QF100'),
    ('B', 'QF200'),
    ('C', 'QF300'),
    ('D', 'QF400'),
    ('E', 'QF500'),
    ('F', 'QF600'),
    ('G', 'QF700'),
    ('H', 'QF800'),
    ('I', 'QF900'),
    ('J', 'QG100'),
    ('K', 'QG200'),
    ('L', 'QG300'),
    ('M', 'QG400'),
    ('N', 'QG500'),
    ('O', 'QG600'),
    ('P', 'QG700'),
    ('Q', 'QG800'),
    ('R', 'QG900'),
]
class FlightsNumber(models.Model):
    class Meta:
        verbose_name = "FlightsNumber"
        verbose_name_plural = "FlightsNumber"

    name = models.CharField(max_length=50)
    number = models.CharField(choices=NUMBER, max_length=200)

    def __str__(self):
        return self.name
