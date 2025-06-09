from django.urls import path
from .views import ApplyJobView, MyApplicationsView, DeleteApplicationView

urlpatterns = [
    path('apply/', ApplyJobView.as_view(), name='apply'),
    path('my-applications/', MyApplicationsView.as_view(), name='my-applications'),
    path('apply/<int:job_id>/', DeleteApplicationView.as_view(), name='delete-application'),
]
