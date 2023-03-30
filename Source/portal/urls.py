from django.urls import path
from . import views

urlpatterns = [
    # risks api routes
    path('', views.view_dashboard, name='dashboard'),
    path('risks', views.view_all_risks, name='all-risks'),
    path('add-risk', views.add_risk, name='add-risk'),
    path('view-risk/<int:pk>', views.view_risk, name='view-risk'),
    path('update-risk/<int:pk>', views.update_risk, name='update-risk'),
]