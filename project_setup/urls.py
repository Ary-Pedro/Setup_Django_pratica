"""
URL configuration for project_setup project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

'''
from django.http import HttpResponse

#htpp REQUEST  < -- Retorna uma response
def testview(request): #quando a url recebe cria uma path ela tá fazendo uma requisição tá passando um argumento, logo preciso do request na função para representar a requisição tal comunicação!
    return HttpResponse('Hello, World!')
'''


urlpatterns = [
    path('admin/', admin.site.urls),
    path ('', include('recipes.urls')),
]
