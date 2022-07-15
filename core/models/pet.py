from django.db import models
from core.models import User


class Pet(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class PetImage(models.Model):
    pet = models.ForeignKey(Pet, related_name="images", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="pets")
