from django.db import models
from .post import Post


class Comment(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    comment=models.CharField(max_length=500)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment