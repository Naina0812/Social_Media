from django.db import models
from django.contrib.auth.models import User

# Create your models here.
GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
# Create your models here.
class Profile(models.Model):
     user = models.OneToOneField(User, on_delete=models.CASCADE)
     firstname = models.CharField(max_length=255)
     lastname = models.CharField(max_length=255)
     email = models.EmailField()
     bio = models.CharField(default="",blank=True,null=True,max_length=350)
     date_of_birth = models.CharField(blank=True,max_length=150)
     gender = models.CharField(("1"), max_length=10)
     updated = models.DateTimeField(auto_now=True)
     created = models.DateTimeField(auto_now_add=True)
     image = models.ImageField(default='default.jpg', upload_to='profile_pics',blank=True, null=True)


     def __str__(self):
        return self.title
     

