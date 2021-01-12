from django.urls import path
from .views import ProjectTemplateView

app_name = 'project'

urlpatterns = [
    path('', ProjectTemplateView.as_view(), name='project'),
]
