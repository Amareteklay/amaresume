from django.db import models


class Contact(models.Model):
    """
    Contact model
    """
    name = models.CharField(blank=True, max_length=100)
    email = models.EmailField()
    subject = models.CharField(blank=True, max_length=200)
    message = models.TextField(max_length=500, blank=True)

    def __str__(self):
        """
        String representation of the Contact model
        """
        return self.subject
