from django.shortcuts import render

# Create your views here.
from .models import Order
from rest_framework import generics, permissions, mixins

from .serializers import OrderSerializer


# Create your views here.
class OrderUpdateMixinView(mixins.UpdateModelMixin, generics.GenericAPIView, ):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    lookup_field = 'pk'

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class OrderDeleteMixinView(mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    lookup_field = 'pk'

    # permission_classes = [permissions.IsAdminUser]

    def get(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class OrderRetrieveMixinView(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    lookup_field = 'pk'

    # permission_classes = [permissions.IsAdminUser]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class OrderListMixinView(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class OrderCreateMixinView(mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

