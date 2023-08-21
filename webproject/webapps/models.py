from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Modelpost(models.Model):
    judul = models.CharField(max_length=300)
    date = models.DateTimeField(auto_now_add=True)
    penulis = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True, upload_to='images')
    konten = models.TextField()
    def __str__(self):
        return self.judul
    