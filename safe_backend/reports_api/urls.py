from django.urls import path
from . import views

urlpatterns = [
    path('report/', views.CreateReportView.as_view(), name='post_report'),
]