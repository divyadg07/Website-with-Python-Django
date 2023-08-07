from django.db import models

# makemigrations - to make changes and save in a file
# migrate - applying pending changes created by migrations

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    info = models.TextField()
    date = models.DateField()
    
    # to change the header name of the models
    def __str__(self):
        return self.name