import pytest

from apps.fixtures.user import user
from apps.post.models import Post


@pytest.fixture
def post(db, user):
    return Post.objects.create(author=user, body="Test Post Body")