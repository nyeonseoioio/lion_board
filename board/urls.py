from django.contrib import admin
from django.urls import path
from .views import ItemCV,ItemDV,ItemLV

app_name = 'spring'
urlpatterns = [
    path("", ItemLV.as_view(), name = "index"),
    path("detail/<int:pk>/", ItemDV.as_view(), name = "detail"),
    path('create/',ItemCV.as_view(), name='create'),
]