from django.db import models

# Create your models here.
class Photo(models.Model):
    name = models.CharField(max_length=150, default='Photograph')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name