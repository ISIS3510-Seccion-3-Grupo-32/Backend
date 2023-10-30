from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from . import models

class DetailedUserReportView(APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self, request, report_id):
        report = models.DetailedUserReport.get_from_firestore(report_id)
        return Response(report)  # Return raw data

class AllDetailedUserReportsView(APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self, request):
        reports = models.DetailedUserReport.get_all_from_firestore()
        return Response(reports)  # Return raw data

class PoliceReportView(APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self, request, report_id):
        report = models.PoliceReport.get_from_firestore(report_id)
        return Response(report)  # Return raw data

class AllPoliceReportsView(APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self, request):
        reports = models.PoliceReport.get_all_from_firestore()
        return Response(reports)  # Return raw data

class SubjectView(APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self, request, subject_id):
        subject = models.Subject.get_from_firestore(subject_id)
        return Response(subject)  # Return raw data

class AllSubjectsView(APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self, request):
        subjects = models.Subject.get_all_from_firestore()
        return Response(subjects)  # Return raw data
