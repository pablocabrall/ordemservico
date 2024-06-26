from django.contrib import admin
from django.urls import path
from backend.servico import views as v
app_name = 'core'

urlpatterns = [
    path('', v.ordem_servico_list, name='ordem_servico_list'),
    #path('create/', v.ordem_servico_create, name='ordem_servico_create'),
    #path('<int:pk>/', v.ordem_servico_detail, name='ordem_servico_detail'),
    #path('<int:pk>/update/', v.ordem_servico_create, name='ordem_servico_update'),
]
