from django.db import models

# Create your models here.
class Coach(models.Model):
    firstName = models.CharField(max_length = 40, blank = False)
    lastName = models.CharField(max_length = 40, blank = False)
    email = models.EmailField(max_length = 50, blank = False, unique = True)
    phone = models.CharField(max_length = 20)
    location = models.CharField(max_length = 40)
    hobby = models.CharField(max_length = 30)
    created = models.DateTimeField(auto_now_add = True)
    lastUpdated = models.DateTimeField(auto_now = True)

    class Meta():
        verbose_name = 'Coaches'

    def __str__(self):
        return f'{self.firstName} {self.lastName}'