from django.urls import path
from . import views

urlpatterns = [
    path('report/Detailed', views.get_all_detailed_user_reports , name='post_report'),
    path('report/Police', views.get_all_police_reports , name='post_report'),
    path('report/Subject', views.get_all_subjects , name='post_report'),
]