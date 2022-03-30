from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class ልጣፍ(models.Model):
    ኣርእስቲ = models.CharField(max_length=100)
    ትሕዝቶ = models.TextField()
    ዕለት = models.DateTimeField(default=timezone.now)
    ደራሲ = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.ኣርእስቲ