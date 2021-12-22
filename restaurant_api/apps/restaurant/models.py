from django.db import models

RESTAURANT_TYPES = (
    ("cs", "Casual"),
    ("ff", "Fast Food"),
    ("fd", "Fine Dining"),
    ("fs", "Family Style"),
)


class Restaurant(models.Model):
    name = models.CharField(max_length=128, unique=True)
    address = models.CharField(max_length=256)
    type = models.CharField(max_length=2, choices=RESTAURANT_TYPES, default="cs")

    def __str__(self):
        return self.name

    def get_type(self):
        return self.get_type_display()
