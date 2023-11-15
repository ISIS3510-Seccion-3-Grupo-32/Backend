from django.urls import path
from . import views

urlpatterns = [
    path('detailed/', views.AllDetailedUserReportsView.as_view() , name='getDetailedReports'),
    path('police/', views.AllPoliceReportsView.as_view() , name='getPoliceReports'),
    path('subject/', views.AllSubjectsView.as_view() , name='getSubjects'),
    path('closest/<latitude>/<longitude>/', views.Analytics.as_view() , name='getClosestCrimeReport'),
]