from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics, permissions
from rest_framework.authentication import SessionAuthentication
from .serializer import CreateReportSerializaer

class CreateReportView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (SessionAuthentication,)
    ##
    def post(self, request, format=None):
        data = request.data
        serializer = CreateReportSerializaer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class GetAllReportsView(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (SessionAuthentication,)
    serializer_class = CreateReportSerializaer
    def get_queryset(self):
        return Response({'reports': CreateReportSerializaer.objects.all()}, status=status.HTTP_200_OK)
    
class GetReportsByDirectionView(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (SessionAuthentication,)
    def get_queryset(self):
        direction = self.kwargs['direction']
        return Response({'reports': CreateReportSerializaer.objects.filter(direction=direction)}, status=status.HTTP_200_OK)
