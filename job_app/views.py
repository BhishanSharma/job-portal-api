from rest_framework import viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Job
from .serializers import JobSerializer
from .permissions import IsEmployerOrReadOnly

class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.select_related('owner').all().order_by('-created_at')
    serializer_class = JobSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsEmployerOrReadOnly]
    
    # ✅ Add filtering, search, pagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['location', 'job_type']
    search_fields = ['title', 'owner__username']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
