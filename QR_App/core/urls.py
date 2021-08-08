from django.urls import path
from .views import menu, create, home


urlpatterns = [
    path('menu', menu, name="menu"),
    path('create', create, name="create"),
    path('', home, name="home")
]
