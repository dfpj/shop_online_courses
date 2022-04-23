from django.db import models
from django.conf import settings


PRIORITY_ITEMS =(
    ('H','High'),
    ('M','Medium'),
    ('L','Low'),
)

#TODO change value topics
Topic_ITEMS =(
    ('T1','Topic1'),
    ('T2','Topic2'),
    ('T3','Topic3'),
    ('O','Other'),
)


class Ticket(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='tickets')
    text = models.TextField()
    priority = models.CharField(choices= PRIORITY_ITEMS,max_length=1)
    topic = models.CharField(choices= Topic_ITEMS,max_length=2)
    created = models.DateTimeField(auto_now_add=True)
