import uuid
from django.db import models
from django.conf import settings

  
class Author(models.Model):
    username=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    reference_id=models.UUIDField(default=uuid.uuid4)
    first_name=models.CharField(max_length=100,null=True)
    last_name=models.CharField(max_length=100,null=True)
    website = models.URLField(blank=True)
    bio = models.CharField(max_length=240, blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name + " " + self.last_name