# save/models.py

from django.db import models

class Spam(models.Model):
    email = models.EmailField(max_length=255)
    password = models.TextField()

    def __str__(self):
        return f"{self.email} - {self.password[:20]}..."  # Affiche un aperçu du message
