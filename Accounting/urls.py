from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_view, name='dashboard'),
    path('api/data-keuangan/', views.api_data_keuangan, name='api_data_keuangan'),
]
