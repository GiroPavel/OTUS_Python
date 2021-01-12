from django.urls import path
from .views import ContactFormView, SuccessTemplateView

app_name = 'contact'

urlpatterns = [
    path('', ContactFormView.as_view(), name='contact_form'),
    path('success/', SuccessTemplateView.as_view(), name='contact_success'),
]
