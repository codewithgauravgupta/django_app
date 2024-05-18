from django.db import models

from apps.abstract.models import AbstractModel, AbstractManager


class CommentManager(AbstractManager):
    pass


class Comment(AbstractModel):
    post = models.ForeignKey("apps_post.Post", on_delete=models.CASCADE)
    author = models.ForeignKey("apps_user.User", on_delete=models.CASCADE)

    body = models.TextField()
    edited = models.BooleanField(default=False)

    objects = CommentManager()

    def __str__(self):
        return self.author.name