from django.shortcuts import render
from .models import Address
from rest_framework import generics, permissions, mixins

from .serializers import AddressSerializer


# Create your views here.
class AddressUpdateMixinView(mixins.UpdateModelMixin, generics.GenericAPIView, ):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    lookup_field = 'pk'

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class AddressDeleteMixinView(mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    lookup_field = 'pk'

    # permission_classes = [permissions.IsAdminUser]

    def get(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class AddressRetrieveMixinView(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    lookup_field = 'pk'

    # permission_classes = [permissions.IsAdminUser]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class AddressListMixinView(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class AddressCreateMixinView(mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

