from django.urls import path

from profiles_api import views          #contains our views

urlpatterns = [
path('hello-view/', views.HelloApiView.as_view())
]
