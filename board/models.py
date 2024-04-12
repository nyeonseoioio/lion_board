from django.db import models

# Create your models here.
class Item(models.Model):
    # image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length = 200)
    content =  models.TextField()
    price = models.IntegerField()

    def __str__ (self):
        return self.title