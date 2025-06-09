from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Application
from django.conf import settings

@receiver(post_save, sender=Application)
def handle_application_created(sender, instance, created, **kwargs):
    if created:
        # Increment applications_count
        job = instance.job
        job.applications_count += 1
        job.save()
        print(instance.applicant.email)
        print(job.owner.email)
        # Email to applicant
        send_mail(
            subject='Your job application was submitted!',
            message=f'Hi {instance.applicant.username}, you successfully applied to {job.title}.',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[instance.applicant.email],
            fail_silently=True,
        )

        # Email to employer
        send_mail(
            subject=f'New application for {job.title}',
            message=f'{instance.applicant.username} has applied to your job posting.',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[job.owner.email],
            fail_silently=True,
        )
