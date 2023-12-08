import os
import datetime
from django.db import models
from google.cloud import firestore
from google.cloud.firestore_v1 import GeoPoint

# Connection with collections of firestore
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./credentials/credentials.json"
database = firestore.Client()

class DetailedUserReport:
    @staticmethod
    def get_from_firestore(report_id):
        doc = database.collection('detailedUserReports').document(report_id).get()
        if doc.exists:
            data = doc.to_dict()
            return {
                'id': report_id,
                'detailed_report': data['DetailedReport']
            }
        else:
            return None

    @staticmethod
    def get_all_from_firestore():
        docs = database.collection('detailedUserReports').stream()
        reports = []
        for doc in docs:
            data = doc.to_dict()
            reports.append({
                'id': doc.id,
                'detailed_report': data['DetailedReport']
            })
        return reports

class PoliceReport:
    @staticmethod
    def get_from_firestore(report_id):
        doc = database.collection('policeReports').document(report_id).get()
        if doc.exists:
            data = doc.to_dict()
            return PoliceReport._format_report(report_id, data)
        else:
            return None
    
    @staticmethod
    def get_all_from_firestore():
        docs = database.collection('policeReports').stream()
        reports = []
        for doc in docs:
            data = doc.to_dict()
            report = PoliceReport._format_report(doc.id, data)
            reports.append(report)
        return reports

    @staticmethod
    def _format_report(report_id, data):
        formatted_data = {
            'id': report_id,
            'record': data['Record']
        }
        # If 'Record' contains a GeoPoint
        if 'Record' in data and isinstance(data['Record'], GeoPoint):
            formatted_data['record'] = {
                'latitude': data['Record'].latitude,
                'longitude': data['Record'].longitude
            }
        return formatted_data


class Subject:
    @staticmethod
    def get_from_firestore(subject_id):
        doc = database.collection('usersReports').document(subject_id).get()
        if doc.exists:
            data = doc.to_dict()
            if 'Subject' in data:
                return {
                    'id': subject_id,
                    'subject': data['Subject']
                }
        return None

    @staticmethod
    def get_all_from_firestore():
        docs = database.collection('usersReports').stream()
        subjects = []
        for doc in docs:
            data = doc.to_dict()
            if 'Subject' in data:
                subjects.append({
                    'id': doc.id,
                    'subject': data['Subject']
                })
        return subjects

class Analytics():
    @staticmethod
    # Create a funciton that calculates the crime report that is the closest to the location given by the user, this should be consulted from the django database
    def get_closest_crime_report(latitude, longitude):
        # Get all the crime reports from the database
        crime_reports = PoliceReport.get_all_from_firestore()
        # Create a list of distances between the user and the crime reports
        distances = []
        for report in crime_reports:
            # Calculate the distance between the user and the crime report
            distance = Analytics.get_distance(latitude, longitude, report['record']['latitude'], report['record']['longitude'])
            # Add the distance to the list
            distances.append(distance)
        # Get the index of the closest crime report
        closest_crime_report_index = distances.index(min(distances))
        # Return the closest crime report
        return distances[closest_crime_report_index]
    
    @staticmethod
    def get_distance(latitude1, longitude1, latitude2, longitude2):
        # Calculate the distance between the user and the crime report
        distance = ((latitude1 - latitude2)**2 + (longitude1 - longitude2)**2)**(1/2)
        return distance
    

class UserForm(models.Model):
    question1 = models.CharField(max_length=255)
    answer1 = models.CharField(max_length=255)
    question2 = models.CharField(max_length=255)
    answer2 = models.CharField(max_length=255)
    question3 = models.CharField(max_length=255)
    answer3 = models.CharField(max_length=255)
    question4 = models.CharField(max_length=255)
    answer4 = models.CharField(max_length=255)
    date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return f"Form - {self.id}"
    
class Suggestions(models.Model):
    description = models.CharField(max_length=2000)

    @staticmethod
    def get_all_firestore():
        docs = database.collection('suggReports').stream()
        suggestions = []

        for doc in docs:
            data = doc.to_dict()
            description = data.get('description', '')  # Use get method to avoid KeyError

            # Create a Suggestions object with the retrieved description
            suggestion = Suggestions(description=description)
            suggestion.save()

            suggestions.append({
                'id': suggestion.id,
                'suggestion': suggestion.description
            })

        return suggestions
