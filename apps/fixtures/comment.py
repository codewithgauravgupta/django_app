import pytest

from apps.fixtures.user import user
from apps.fixtures.post import post

from apps.comment.models import Comment

@pytest.fixture
def comment(db, user, post):
    return Comment.objects.create(author=user, post=post, body="Test Comment Body")