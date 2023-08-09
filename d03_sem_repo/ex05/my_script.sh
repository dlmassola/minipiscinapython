# configuração e instalação do DJANGO
DIRETORIO_AMBIENTE="django_venv"

python3 -m venv $DIRETORIO_AMBIENTE

. $DIRETORIO_AMBIENTE/bin/activate

python3 -m pip install --force-reinstall -r requirement.txt

# Criação do projeto
django-admin startproject django_project

# Criação da aplicação
cd django_project

django-admin startapp helloworld

# Abrir o arquivo django_project/settings.py e adicionar a aplicação criada na lista de INSTALLED_APPS
# INSTALLED_APPS = [
#     'helloworld.apps.HelloworldConfig',
#     'django.contrib.admin',
#     .......

# Abrir o arquivo helloworld/views.py e adicionar o código abaixo
# from django.http import HttpResponse
# from django.shortcuts import render
# from django.http import HttpResponse
# def index(request):
#     return HttpResponse("Hello World!")

# Abrir o arquivo django_project/urls.py e adicionar o código abaixo
# from django.contrib import admin
# from django.urls import path, include
# urlpatterns = [
#    path('admin/', admin.site.urls),
#    path('helloworld', include('helloworld.urls'))
# ]

# Criar o arquivo helloworld/urls.py e adicionar o código abaixo
# from django.urls import path
# from . import views
# urlpatterns = [
#     path('', views.index, name='index'),
# ]

# Executar o comando abaixo para iniciar o servidor
# python3 manage.py runserver
