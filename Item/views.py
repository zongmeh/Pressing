from django.shortcuts import render

# Create your views here.
from .models import Items
from rest_framework import generics, permissions, mixins

from .serializers import ItemSerializer


# Create your views here.
class ItemUpdateMixinView(mixins.UpdateModelMixin, generics.GenericAPIView, ):
    queryset = Items.objects.all()
    serializer_class = ItemSerializer
    lookup_field = 'pk'

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class ItemDeleteMixinView(mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Items.objects.all()
    serializer_class = ItemSerializer
    lookup_field = 'pk'

    # permission_classes = [permissions.IsAdminUser]

    def get(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class ItemRetrieveMixinView(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Items.objects.all()
    serializer_class = ItemSerializer
    lookup_field = 'pk'

    # permission_classes = [permissions.IsAdminUser]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class ItemListMixinView(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Items.objects.all()
    serializer_class = ItemSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class ItemCreateMixinView(mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Items.objects.all()
    serializer_class = ItemSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

