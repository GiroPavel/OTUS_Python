from django.views.generic import TemplateView


class ProjectTemplateView(TemplateView):
    template_name = 'project/project.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['active_page'] = '/project/'
        return context
