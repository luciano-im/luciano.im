from django.views.generic.edit import FormView
from website.forms import ContactForm
# from django.core.mail import send_mail
from django.core.mail import EmailMessage

class IndexView(FormView):
    template_name = 'index.html'
    form_class = ContactForm
    success_url = '/'

    def form_valid(self, form):
        email = form.cleaned_data.get('email')
        subject = form.cleaned_data.get('subject')
        message = form.cleaned_data.get('message')

        content = "{0} quiere contactarte: ".format(form.cleaned_data.get('email'))
        content += "\n\n Asunto: {0}".format(form.cleaned_data.get('subject'))
        content += "\n\n Mensaje: {0}".format(form.cleaned_data.get('message'))

        email_message = EmailMessage(
            'Mensaje de Luciano.im',
            content,
            'El Grillo <hola@luciano.im>',
            ['hola@luciano.im'],
            reply_to=[email]
        )
        email_message.send()

        return super(IndexView, self).form_valid(form)