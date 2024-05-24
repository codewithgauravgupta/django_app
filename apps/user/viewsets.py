from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import viewsets

from apps.abstract.viewsets import AbstractViewSet
from apps.user.serializers import UserSerializer
from apps.user.models import User
from apps.auth.permissions import UserPermission

# class UserViewSet(viewsets.ModelViewSet):
class UserViewSet(AbstractViewSet):
    http_method_names = ('get','patch')
    # permission_classes = (AllowAny,)
    permission_classes = (
        IsAuthenticated,
        UserPermission,
    )
    serializer_class = UserSerializer

    # This method is used by the viewset to get a list of all the users. This method will be called when /user/ is hit with a GET request.
    def get_queryset(self):
        if self.request.user.is_superuser:
            return User.objects.all()
        return User.objects.exclude(is_superuser=True)

    # This method is used by the viewset to get one user. This method is called when a GET or PUT request is made on the /user/id/ endpoint, with id representing the ID of the user.
    def get_object(self):
        obj = User.objects.get_object_by_public_id(self.kwargs['pk'])

        self.check_object_permissions(self.request, obj)

        return obj
    
    