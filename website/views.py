from django.views.generic.edit import FormView
from website.forms import ContactForm
from django.core.mail import EmailMessage
from django.core.mail import BadHeaderError
import smtplib

class IndexView(FormView):
    template_name = 'index.html'
    form_class = ContactForm
    success_url = '/'

    def form_valid(self, form):
        email = form.cleaned_data.get('email')
        subject = form.cleaned_data.get('subject')
        message = form.cleaned_data.get('message')

        content = f'{email} quiere contactarte: '
        content += f'\n\n Asunto: {subject}'
        content += f'\n\n Mensaje: {message}'

        email_subject = 'Mensaje de Luciano.im'
        to_email = 'hola@luciano.im'
        
        try:
            mail = EmailMessage(email_subject, content, to=[to_email], from_email=email, reply_to=[email])
            mail.send()
        except BadHeaderError:
            print('Invalid header found.')
        except smtplib.SMTPException:
            print('Error: Unable to send email')

        return super(IndexView, self).form_valid(form)