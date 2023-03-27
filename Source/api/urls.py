from django.urls import path
from . import views

urlpatterns = [
    # risks api routes
    path('risk/add', views.AddRiskAPI),
    path('risks', views.RisksAPI),
    path('risk/<int:pk>', views.RiskAPI),
]