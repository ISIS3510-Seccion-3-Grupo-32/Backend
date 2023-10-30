from django.db import models
import os
from google.cloud import firestore

# Connection with collections of firestore
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./credentials/credentials.json"
databse=firestore.Client()

class DetailedUserReport(models.Model):
    detailed_report = models.TextField()

    @staticmethod
    def get_from_firestore(report_id):
        doc = databse.collection('detailedUserReports').document(report_id).get()
        if doc.exists:
            data = doc.to_dict()
            return DetailedUserReport(
                id=report_id,
                detailed_report=data['DetailedReport']
            )
        else:
            return None
        
    @staticmethod
    def get_all_from_firestore():
        docs = databse.collection('detailedUserReports').stream()
        reports = []
        for doc in docs:
            data = doc.to_dict()
            reports.append(DetailedUserReport(
                id=doc.id,
                detailed_report=data['DetailedReport']
            ))
        return reports

class PoliceReport(models.Model):
    record = models.JSONField()  # Use JSONField to store a list of strings

    @staticmethod
    def get_from_firestore(report_id):
        doc = databse.collection('policeReports').document(report_id).get()
        if doc.exists:
            data = doc.to_dict()
            return PoliceReport(
                id=report_id,
                record=data['Record']
            )
        else:
            return None
        
    @staticmethod
    def get_all_from_firestore():
        docs = databse.collection('policeReports').stream()
        reports = []
        for doc in docs:
            data = doc.to_dict()
            reports.append(PoliceReport(
                id=doc.id,
                record=data['Record']
            ))
        return reports

class Subject(models.Model):
    subject = models.CharField(max_length=255)

    @staticmethod
    def get_from_firestore(subject_id):
        doc = databse.collection('subjects').document(subject_id).get()
        if doc.exists:
            data = doc.to_dict()
            return Subject(
                id=subject_id,
                subject=data['Subject']
            )
        else:
            return None
        
    @staticmethod
    def get_all_from_firestore():
        docs = databse.collection('subjects').stream()
        subjects = []
        for doc in docs:
            data = doc.to_dict()
            subjects.append(Subject(
                id=doc.id,
                subject=data['Rubject']
            ))
        return subjects
