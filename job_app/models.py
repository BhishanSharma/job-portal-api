from django.db import models
from django.contrib.auth.models import User

class Job(models.Model):
    JOB_TYPES = (
        ('FT', 'Full Time'),
        ('PT', 'Part Time'),
        ('RM', 'Remote'),
        ('CT', 'Contract'),
    )

    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='jobs')
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=100)
    job_type = models.CharField(max_length=2, choices=JOB_TYPES)
    created_at = models.DateTimeField(auto_now_add=True)
    applications_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title
