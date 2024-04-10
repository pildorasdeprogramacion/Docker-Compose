from django.urls import path
from . import views

app_name = 'formulario'

urlpatterns = [
path('create/', views.crear_persona, name='create_person'),
]
