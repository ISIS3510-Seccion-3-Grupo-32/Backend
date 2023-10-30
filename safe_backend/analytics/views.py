from django.shortcuts import render
import models


def get_detailed_user_report(request, report_id):
    report = models.DetailedUserReport.get_from_firestore(report_id)
    if report:
        return render(request, 'detailed_user_report.html', {'report': report})
    else:
        return render(request, 'detailed_user_report.html', {'report': None})
    
def get_all_detailed_user_reports(request):
    reports = models.DetailedUserReport.get_all_from_firestore()
    return render(request, 'all_detailed_user_reports.html', {'reports': reports})

def get_police_report(request, report_id):
    report = models.PoliceReport.get_from_firestore(report_id)
    if report:
        return render(request, 'police_report.html', {'report': report})
    else:
        return render(request, 'police_report.html', {'report': None})
    
def get_all_police_reports(request):
    reports = models.PoliceReport.get_all_from_firestore()
    return render(request, 'all_police_reports.html', {'reports': reports})

def get_subject(request, subject_id):
    subject = models.Subject.get_from_firestore(subject_id)
    if subject:
        return render(request, 'subject.html', {'subject': subject})
    else:
        return render(request, 'subject.html', {'subject': None})
    
def get_all_subjects(request):
    subjects = models.Subject.get_all_from_firestore()
    return render(request, 'all_subjects.html', {'subjects': subjects})


