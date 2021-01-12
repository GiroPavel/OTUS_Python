from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView, DeleteView

from .models import Application

from .forms import MainForm


class MainFormView(CreateView):
    model = Application
    template_name = 'main/main.html'
    success_url = '/'
    form_class = MainForm

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['active_page'] = '/'
        return context


class MainUpdateFormView(UpdateView):
    model = Application
    template_name = 'main/main.html'
    success_url = '/administrations/applications/'
    form_class = MainForm


class AdministrationsTemplateView(TemplateView):
    template_name = 'main/administrations.html'


class ApplicationsListView(ListView):
    model = Application
    template_name = 'main/applications.html'


class ApplicationOneDetailView(DetailView):
    model = Application
    template_name = 'main/one_application.html'


class ApplicationDeleteView(DeleteView):
    model = Application
    template_name = 'main/delete_application.html'
    success_url = '/administrations/applications/'
