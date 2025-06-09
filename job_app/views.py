from rest_framework import viewsets, permissions
from .models import Job
from .serializers import JobSerializer
from .permissions import IsEmployerOrReadOnly

class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all().order_by('-created_at')
    serializer_class = JobSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsEmployerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
