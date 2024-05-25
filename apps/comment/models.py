from django.db import models
from apps.abstract.models import AbstractModel, AbstractManager


class CommentManager(AbstractManager):
    pass


class Comment(AbstractModel):
    post = models.ForeignKey("apps_post.Post", on_delete=models.CASCADE)
    author = models.ForeignKey("apps_user.User", on_delete=models.CASCADE)

    body = models.TextField()
    edited = models.BooleanField(default=False)

    # telling Django with Manager class to use to manage the Comment model 
    objects = CommentManager()

    # creating a default __str__ method to return the name of the author when checking a comment object in the Django shell.
    def __str__(self):
        return self.author.name