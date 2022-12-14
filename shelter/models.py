from django.contrib.auth import get_user_model
from django.db import models


CATEGORY_CHOICES = (
    ('', ''),
    ('Dog', 'Dog'),
    ('Cat', 'Cat'),
    ('Bird', 'Bird'),
    ('Rabbit', 'Rabbit'),
    ('Other', 'Other'),
)


class Animal(models.Model):
    animal_id = models.IntegerField(primary_key=True)
    animal_name = models.CharField(max_length=36)
    animal_type = models.CharField(max_length=16, choices=CATEGORY_CHOICES,
                                   default='')
    breed = models.CharField(max_length=32)
    personality = models.TextField(default="")
    cared_for_by = models.ForeignKey(get_user_model(),
                                     on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.animal_name
