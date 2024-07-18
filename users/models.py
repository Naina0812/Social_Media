from django.db import models

# Create your models here.
GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
# Create your models here.
class User(models.Model):
    #  user_id = models.AutoField(primary_key=True)
     firstname = models.CharField(max_length=255)
     lastname = models.CharField(max_length=255)
     email = models.EmailField()
     mobile_no = models.IntegerField()
     dob = models.DateField()
     gender = models.CharField(("1"), max_length=10)
     profile_image = models.ImageField()
     profile_desc= models.TextField()
    #  created_at = models.DateTimeField(False, True, editable=False)
    #  updated_at = models.DateTimeField(True, True, editable=False)
