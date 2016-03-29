from django.views.generic.edit import FormView
from website.forms import ContactForm
from django.core.mail import send_mail

class IndexView(FormView):
	template_name = 'index.html'
	form_class = ContactForm
	success_url = '/'

	def form_valid(self, form):
		message = "{0} quiere contactarte: ".format(form.cleaned_data.get('email'))
		message += "\n\n Asunto: {0}".format(form.cleaned_data.get('subject'))
		message += "\n\n Mensaje: {0}".format(form.cleaned_data.get('message'))
		
		send_mail('Mensaje de luciano.im',message,'hola@luciano.im',['hola@luciano.im'])
		return super(IndexView, self).form_valid(form)