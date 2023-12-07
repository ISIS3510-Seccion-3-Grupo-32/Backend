from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from . import models
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

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
    
class Analytics(APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self, request, latitude, longitude):
        reports = models.Analytics.get_closest_crime_report(float(latitude), float(longitude))
        return Response(reports)  # Return raw data
    
    def get(self, request):
        suggReports = models.Suggestions.get_all_firestore()
        return Response(suggReports)
        
    
    @csrf_exempt
    def post_user_form(request):
        if request.method == 'POST':
            try:
                data = json.loads(request.body)
                print(data)

                user_form = models.UserForm(
                    question1=data.get('question1'),
                    answer1=data.get('answer1'),
                    question2=data.get('question2'),
                    answer2=data.get('answer2'),
                    question3=data.get('question3'),
                    answer3=data.get('answer3'),
                    question4=data.get('question4'),
                    answer4=data.get('answer4'),
                )
                user_form.save()

                return JsonResponse({'status': 'success', 'message': 'Form submitted successfully'})
            except json.JSONDecodeError as e:
                return JsonResponse({'status': 'error', 'message': 'Invalid JSON data'})
            except KeyError as e:
                return JsonResponse({'status': 'error', 'message': f'Missing key in JSON data: {e}'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Invalid request method'})
