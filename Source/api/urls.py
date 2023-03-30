from django.urls import path
from . import views

urlpatterns = [
    # risks api routes
    path('risk/add', views.AddRiskAPI),
    path('risks', views.RisksAPI),
    path('risks/top10', views.RisksTopScoresAPI),
    path('risks/impactStats', views.RisksImpactStatsAPI),
    path('risks/likelikehoodStats', views.RisksLikelihoodStatsAPI),
    path('risks/statusStats', views.RisksStatusStatsAPI),
    path('risk/<int:pk>', views.RiskAPI),
]