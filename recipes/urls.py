from django.urls import path
from recipes.views import home, contato, sobre

urlpatterns = [
    path('', home),  # Homepage
    path('contato/', contato),  # Contact
    path('sobre/', sobre),  # About
]