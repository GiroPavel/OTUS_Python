from django.views.generic import FormView, TemplateView

from .forms import ContactForm

from .tasks import send_mail_task


class ContactFormView(FormView):
    template_name = 'contact/contact.html'
    success_url = 'success'
    form_class = ContactForm

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['active_page'] = '/contact/'
        return context

    def form_valid(self, form):
        email = form.cleaned_data['email']
        subject = form.cleaned_data['subject']
        message = form.cleaned_data['message']

        send_mail_task.delay(subject, message, email)
        return super().form_valid(form)


class SuccessTemplateView(TemplateView):
    template_name = 'contact/success.html'
