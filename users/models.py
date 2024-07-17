from django.db import models

GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
# Create your models here.
class User(models.Model):
     user_id = models.AutoField(primary_key=True)
     firstname = models.CharField(max_length=255)
     lastname = models.CharField(max_length=255)
     email = models.EmailField(max_length=255)
     mobile_no = models.IntegerField(max_length=10)
     dob = models.DateField()
     gender = models.CharField(("1"), max_length=10)
     profile_image = models.ImageField(upload_to='url')
     profile_desc= models.CharField(max_length=50)
     created_at = models.DateTimeField(False, True, editable=False)
     updated_at = models.DateTimeField(True, True, editable=False)
