from django.db import models
from django.contrib.auth.models import User


class Modeling(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_model')
    title = models.CharField(max_length=200)
    description = models.TextField()
    model_file = models.FileField(upload_to='models/')
    model_extension = models.CharField(max_length=10)
    thumbnail = models.FileField(upload_to='thumbnail/')
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_model', null=True, blank=True)

    def __str__(self):
        return self.title
    

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_model_comment')
    modeling = models.ForeignKey(Modeling, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_model_comment')