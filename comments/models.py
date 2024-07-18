from django.db import models

# Create your models here.
# from django.contrib.auth.models import users

class Comment(models.Model):
    # comment_id = models.AutoField(primary_key=True)
    # user_id = models.ForeignKey(users, on_delete=models.CASCADE)
    comment_text=models.CharField(max_length=50)
    # created_at = models.DateTimeField(False, True, editable=False)
    # updated_at = models.DateTimeField(True, True, editable=False)
