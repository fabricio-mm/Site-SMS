from django.urls import path
from . import views

urlpatterns =[
    path('diagramas/', views.diagramas)
]