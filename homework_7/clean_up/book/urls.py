from django.urls import path
from .views import BookFormView, CleanListView, CleanDeleteView

app_name = 'book'

urlpatterns = {
    path('', BookFormView.as_view(), name='create_book_form'),
    path('your_books/', CleanListView.as_view(), name='clean_list'),
    path('delete_books/<int:pk>/', CleanDeleteView.as_view(), name='book_delete'),
}
