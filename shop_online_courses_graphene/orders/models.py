from django.db import models
from django.conf import settings
from django.utils import timezone
from django.core.validators import MinValueValidator,MaxValueValidator

from courses.models import Course

class OrderItem(models.Model):
    course = models.OneToOneField(Course,on_delete=models.CASCADE)
    order = models.ForeignKey('Order',on_delete=models.CASCADE,related_name='items')
    price =models.IntegerField()


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    coupon = models.ForeignKey('Coupon',on_delete=models.CASCADE,null=True)
    paid = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now=True)
    pay_time =models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.id}'

    def get_total_price(self):
        sum_order_item_price = sum([item.price for item in OrderItem.objects.filter(order=self)])
        return sum_order_item_price * (self.coupon.discount/100) if self.coupon else sum_order_item_price


class Coupon(models.Model):
    code = models.CharField(max_length=20)
    discount = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(100)])
    valid_to = models.DateTimeField()
    valid_from = models.DateTimeField()
    is_active =models.BooleanField(default=False)