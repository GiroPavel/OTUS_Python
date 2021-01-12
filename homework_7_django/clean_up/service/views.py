from django.views.generic import TemplateView


class ServiceTemplateView(TemplateView):
    template_name = 'service/service.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['active_page'] = '/service/'
        return context
