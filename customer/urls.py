from django.urls import path
from . import views
from .views import Order, OrderConfirmation, OrderPayConfirmation

urlpatterns = [
    path('', views.Index.as_view(), name="index"),
    path('about', views.About.as_view(), name="about"),
    path('order/', Order.as_view(), name='order'),
    path('order-confirmation/<int:pk>', OrderConfirmation.as_view(),
         name='order-confirmation'),
    path('payment-confirmation/', OrderPayConfirmation.as_view(),
         name='payment-confirmation')
]