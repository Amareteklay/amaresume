from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


ምድብ = ((0, 'ረቒቕ'), (1, 'ሕታም'))


class ልጣፍ(models.Model):
    """ Model for blog posts """
    ኣርእስቲ = models.CharField(max_length=200, unique=True)
    ስለግ = models.SlugField(max_length=200,  blank=True, null=True)
    ደራሲ = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="tigblog_posts")
    ትሕዝቶ = models.TextField()
    ምስሊ = CloudinaryField('image', default='placeholder')
    መጠቓለሊ = models.TextField(blank=True)
    ዕለት = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    ምድብ = models.IntegerField(choices=ምድብ, default=0)
    ፈተውቲ = models.ManyToManyField(User, related_name='tigpost_likes', blank=True)

    class Meta:
        ordering = ['-ዕለት']

    def __str__(self):
        """ String representation of the Post model """
        return self.ኣርእስቲ

    def number_of_likes(self):
        """ Count number of likes """
        return self.ፈተውቲ.count()

    def save(self, *args, **kwargs):
        self.ስለግ = slugify(self.ኣርእስቲ)
        super(ልጣፍ, self).save(*args, **kwargs)


class ርእይቶ(models.Model):
    """ Model for comments on blog posts """
    ልጣፍ = models.ForeignKey(ልጣፍ, on_delete=models.CASCADE,
                             related_name='tigcomments')
    ሽም = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name="tigpost_comments")
    ኢመይል = models.EmailField()
    ትሕዝቶ = models.TextField(max_length=200)
    ዕለት = models.DateTimeField(auto_now_add=True)
    ፀዲቑ = models.BooleanField(default=False)

    class Meta:
        ordering = ['ዕለት']

    def __str__(self):
        return f"ርእይቶ ብ {self.ሽም}፥ {self.ትሕዝቶ}"
