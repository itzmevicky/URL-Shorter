from django.urls import path

from URL import views

urlpatterns = [
    path('',views.ShortURL)
]