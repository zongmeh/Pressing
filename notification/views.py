from django.shortcuts import render

# Create your views here.
from .models import Notification
from rest_framework import generics, permissions, mixins

from .serializers import NotificationSerializer


# Create your views here.
class NotificationUpdateMixinView(mixins.UpdateModelMixin, generics.GenericAPIView, ):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    lookup_field = 'pk'

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class NotificationDeleteMixinView(mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    lookup_field = 'pk'

    # permission_classes = [permissions.IsAdminUser]

    def get(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class NotificationRetrieveMixinView(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    lookup_field = 'pk'

    # permission_classes = [permissions.IsAdminUser]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class NotificationListMixinView(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class NotificationCreateMixinView(mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

