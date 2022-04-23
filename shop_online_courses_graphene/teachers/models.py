from django.db import models
from django.conf import settings

DEGREE_ITEMS =(
    ('A','Associate'),
    ('B','Bachelor'),
    ('M','Master'),
    ('D','Doctor'),
    ('P','Professional'),
)

class Teacher(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    bio = models.TextField()
    degree = models.CharField(choices=DEGREE_ITEMS,max_length=1)

    def __str__(self):
        return self.bio[:10]

