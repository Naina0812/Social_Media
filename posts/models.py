from django.db import models

# Create your models here.
# MEDIA_CHOICES = (
#         ('image', 'Male'),
#         ('video', 'Female'),
#     )

class Post(models.Model):
    # post_id= models.AutoField(primary_key=True)
    # user_id = models.ForeignKey(users, on_delete=models.CASCADE)
    description = models.TextField()
    # created_at = models.DateTimeField(False, True, editable=False)
    # updated_at = models.DateTimeField(True, True, editable=False)
    # media_url = models.CharField(("1"),upload_to='url')
