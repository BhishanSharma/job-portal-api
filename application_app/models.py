from django.db import models
from django.contrib.auth.models import User
from job_app.models import Job

class Application(models.Model):
    applicant = models.ForeignKey(User, on_delete=models.CASCADE, related_name='applications')
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applications')
    cover_letter = models.TextField()
    applied_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('applicant', 'job')  # prevent duplicate applications

    def __str__(self):
        return f"{self.applicant.username} -> {self.job.title}"
