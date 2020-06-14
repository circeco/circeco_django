from django.db import models
from django.contrib.auth.models import User
from shops.models import Shop



class UserFavouriteShop(models.Model):
    user = models.ForeignKey(User, null=False)
    shop = models.ForeignKey(Shop, null=False)

    class Meta:
        unique_together = ('user', 'shop')
        # constraints = [models.UniqueConstraint(fields=['user', 'shop'], name='user_shop')]

