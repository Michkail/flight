from django.db import models

DATE = [
    ('A', '2020-06-10'),
    ('B', '2020-06-11'),
    ('C', '2020-06-12'),
    ('D', '2020-06-13'),
    ('E', '2020-06-14'),
    ('F', '2020-06-15'),
    ('G', '2020-06-16')
]
CLOCK = [
    ('T00', '09:00:23Z'),
    ('T01', '10:00:23Z'),
    ('T02', '11:00:23Z')
]
class DeparturesTime(models.Model):
    class Meta:
        verbose_name = "DeparturesTime"
        verbose_name_plural = "DeparturesTime"

    name = models.CharField(max_length=50)
    date = models.CharField(choices=DATE, max_length=50)
    clock = models.CharField(choices=CLOCK, max_length=50)

    def __str__(self):
        return self.name
