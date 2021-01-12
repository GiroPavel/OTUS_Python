from django.views.generic import TemplateView


class AboutTemplateView(TemplateView):
    template_name = 'about/about.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['active_page'] = '/about/'
        return context
