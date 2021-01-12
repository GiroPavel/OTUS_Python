from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls', namespace='main')),
    path('about/', include('about.urls', namespace='about')),
    path('service/', include('service.urls', namespace='service')),
    path('project/', include('project.urls', namespace='project')),
    path('contact/', include('contact.urls', namespace='contact')),
    path('book/', include('book.urls', namespace='book')),
]

