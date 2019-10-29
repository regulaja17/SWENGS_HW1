from django.db import models

class Student(models.Model):
    CHOICES = (
        ("ima", "Information Management"),
        ("geb", "E-Health"),
        ("bau", "Bauingenieurswesen")
    )

    first_name = models.TextField()
    last_name = models.TextField()
    birthdate = models.DateField()
    studies = models.CharField(max_length=3, choices=CHOICES)

    def __str__(self):
        return (self.first_name + self.last_name)
