from django import forms

class ContactForm(forms.Form):
	email = forms.EmailField(max_length=100, widget=forms.TextInput(attrs={'placeholder':'Ingresa tu correo'}))
	subject = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'placeholder':'Hacenos una introduccion'}))
	message = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Que necesitas?'}))