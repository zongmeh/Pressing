from django.urls import path, include

urlpatterns = [
    path('address/', include('Address.urls')),
    path('dresses/', include('Item.urls')),
    path('user/', include('user.urls')),
    path('notification/', include('notification.urls')),
    path('order/', include('Order.urls')),
]
