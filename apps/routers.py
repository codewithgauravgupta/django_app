from rest_framework import routers
from apps.user.viewsets import UserViewSet
from apps.auth.viewsets import RegisterViewSet, LoginViewSet, RefreshViewSet
from apps.post.viewsets import PostViewSet

router = routers.DefaultRouter()

# ##################################################################### #
# ################### AUTH                       ###################### #
# ##################################################################### #

router.register(r'auth/register', RegisterViewSet, basename='auth-register')
router.register(r'auth/login', LoginViewSet, basename='auth-login')
router.register(r'auth/refresh', RefreshViewSet, basename='auth-refresh')


# ##################################################################### #
# ################### USER                       ###################### #
# ##################################################################### #

router.register(r'user', UserViewSet, basename='user')

# ##################################################################### #
# ################### POST                       ###################### #
# ##################################################################### #

router.register(r'post', PostViewSet, basename='post')

urlpatterns = [
    *router.urls,
]