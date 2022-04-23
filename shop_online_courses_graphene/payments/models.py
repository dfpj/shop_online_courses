from django.db import models
from django.conf import settings

from orders.models import Order


class Pay(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    order = models.OneToOneField(Order,on_delete=models.CASCADE)
    paid = models.BooleanField(default=False)
    ref_id = models.CharField(max_length=255,null=True)
    authority = models.CharField(max_length=255)
    status = models.PositiveSmallIntegerField()
    date_of_pay = models.DateTimeField()
    amount = models.IntegerField()

