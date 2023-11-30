from rest_framework import serializers
from .models import Report

class CreateReportSerializaer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'
    def create(self, clean_data):
        report_obj = Report.objects.create(user=clean_data['username'], report=clean_data['report'], description=clean_data['description'])
        report_obj.direction = clean_data['direction']
        report_obj.date_time = clean_data['date_time']
        report_obj.save()
        return report_obj
    
class GetAllReportsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'
    def get_queryset(self):
        return Report.objects.all()
    
class GetReportsByDirectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ('direction', 'reoprt')
    def get_queryset(self):
        direction = self.kwargs['direction']
        return Report.objects.filter(direction=direction)