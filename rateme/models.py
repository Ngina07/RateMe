from django.db import models
from django.contrib.auth import User

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length = 60)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    url = models.CharField(max_length = 60)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
