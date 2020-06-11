from django.db import models
from django.contrib.auth.models import User

class Shop(models.Model):
    name = models.CharField(max_length=25)

class UserFavouriteShop(models.Model):
    user = models.ForeignKey(User, null=False)
    shop = models.ForeignKey(Shop, null=False)


