from django.db import models

# Create your models here.
class student(models.Model):
    Name = models.CharField(max_length=100, verbose_name="Name")
    Email= models.EmailField(max_length=100, verbose_name="Email")
   
    def __str__(self):
        return str(self.id)