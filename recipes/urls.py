
from django.urls import path
from recipes.views import home_receitas

urlpatterns = [
    path ('', home_receitas),
]
