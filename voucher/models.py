from django.db import models
from django.contrib.auth.models import User

class Voucher(models.Model):
    amount = models.DecimalField(max_digits=6, decimal_places=0)
    user = models.ForeignKey(User, null=False) 
    image = models.BinaryField(null=True)

    def __str__(self):

        return f'{self.user.username}_{self.id}_{self.amount}'
