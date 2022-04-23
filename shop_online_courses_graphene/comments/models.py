from django.db import models
from django.conf import settings
from courses.models import Course


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='comments')
    course = models.ForeignKey(Course,on_delete=models.CASCADE,related_name='comments')
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
