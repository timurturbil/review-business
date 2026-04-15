from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Review(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
   name = models.CharField(max_length=20)
   review = models.TextField()
   date_created = models.DateTimeField(auto_now_add=True)

   def __str__(self):
      return f"{self.user.username} - {self.name}"


