from django.urls import path
from . import views

urlpatterns = [
    # risks api routes
    path('risks', views.view_all_risks, name='all-risks'),
    path('add-risks', views.add_risk, name='add-risk'),
]