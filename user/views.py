from django.shortcuts import render

# Create your views here.
from .models import User
from rest_framework import generics, permissions, mixins

from .serializers import UserSerializer


# Create your views here.
class UserUpdateMixinView(mixins.UpdateModelMixin, generics.GenericAPIView, ):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'pk'

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class UserDeleteMixinView(mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'pk'

    # permission_classes = [permissions.IsAdminUser]

    def get(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class UserRetrieveMixinView(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'pk'

    # permission_classes = [permissions.IsAdminUser]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class UserListMixinView(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class UserCreateMixinView(mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

