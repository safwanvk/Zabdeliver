from django.urls import path
from . import views
from .views import Order

urlpatterns = [
    path('', views.Index.as_view(), name="index"),
    path('about', views.About.as_view(), name="about"),
    path('order/', Order.as_view(), name='order'),
]