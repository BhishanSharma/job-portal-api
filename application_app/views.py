# application_app/views.py

from rest_framework import generics, permissions
from .models import Application
from .serializers import ApplicationSerializer
from rest_framework.exceptions import ValidationError

class ApplyJobView(generics.CreateAPIView):
    serializer_class = ApplicationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        job = serializer.validated_data['job']
        user = self.request.user

        if Application.objects.filter(applicant=user, job=job).exists():
            raise ValidationError("You have already applied to this job.")

        serializer.save(applicant=user)

class DeleteApplicationView(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        job_id = self.kwargs['job_id']
        return Application.objects.get(applicant=self.request.user, job_id=job_id)

class MyApplicationsView(generics.ListAPIView):
    serializer_class = ApplicationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Application.objects.filter(applicant=self.request.user).select_related('job')
