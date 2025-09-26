from django.urls import path
from . import views

# urlpatterns deve ser uma lista (com colchetes [])
urlpatterns = [
    path('', views.home, name='home'),
    path('historia/', views.historia, name='historia'),
    path('atracoes/', views.atracoes, name='atracoes'),
    path('galeria/', views.galeria, name='galeria'),
]
