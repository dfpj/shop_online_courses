from django.db import models
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=100)


class Course(models.Model):
    title = models.CharField(max_length=255)
    categoty = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='courses')
    tags = models.ManyToManyField('Tag')
    slug = models.CharField(max_length=255)
    is_active = models.BooleanField(default=False)
    description = models.TextField()
    view = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    published = models.DateTimeField(default=timezone.now)
    cover = models.ImageField(default='course.jpg')
    trailer = models.FileField(default='trailer.mp4')

    def __str__(self):
        return self.title


class Lesson(models.Model):
    title = models.CharField(max_length=255)
    course = models.ForeignKey(Course,on_delete=models.CASCADE,related_name='lessons')
    slug = models.CharField(max_length=255)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    published = models.DateTimeField(default=timezone.now)
    video = models.FileField(null=True)
    #TODO calculate duration in post_save signal when upload video
    duration = models.DurationField(null=True)

    def __str__(self):
        return self.title


class Tag(models.Model):
    name= models.CharField(max_length=255)
