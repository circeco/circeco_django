from django.db import models
from django.contrib.auth.models import User

class Voucher(models.Model):
    amount = models.DecimalField(max_digits=6, decimal_places=0)
    user = models.ForeignKey(User, null=False) 

    def __str__(self):
        # return self.user.username + '_' + self.amount
        return f'{self.user.username}_{self.id}_{self.amount}'
