from django.urls import path
from .views import MainFormView, \
    AdministrationsTemplateView, \
    ApplicationsListView, \
    ApplicationOneDetailView, \
    MainUpdateFormView, \
    ApplicationDeleteView

app_name = 'main'

urlpatterns = [
    path('', MainFormView.as_view(), name='create_form'),
    path('update/<int:pk>/', MainUpdateFormView.as_view(), name='update_applications'),
    path('administrations/', AdministrationsTemplateView.as_view(), name='administrations'),
    path('administrations/applications/', ApplicationsListView.as_view(), name='applications'),
    path('administrations/applications/<int:pk>/', ApplicationOneDetailView.as_view(), name='one_applications'),
    path('administrations/delete_applications/<int:pk>/', ApplicationDeleteView.as_view(), name='delete_applications'),
]
