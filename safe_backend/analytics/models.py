import os
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
