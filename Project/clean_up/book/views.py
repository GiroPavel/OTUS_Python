from django.views.generic import CreateView, ListView, DeleteView

from .models import Clean

from .forms import BookForm


class BookFormView(CreateView):
    model = Clean
    template_name = 'book/book.html'
    success_url = 'your_books'
    form_class = BookForm

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['active_page'] = '/book/'
        return context


class CleanListView(ListView):
    model = Clean
    template_name = 'book/your_books.html'


class CleanDeleteView(DeleteView):
    model = Clean
    template_name = 'book/delete_books.html'
    success_url = '/book/your_books/'
