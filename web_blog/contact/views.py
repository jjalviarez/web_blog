from django.contrib import messages
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .forms import ContactForm
from django.core.mail import EmailMessage
#from .models import Contact

# Create your views here.

def contact(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ContactForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            email=EmailMessage(
                'Email de Contacto',
                'Usuario:{}\nEmail:{}\nMensaje:{}'.format(
                    form.cleaned_data['name'],
                    form.cleaned_data['email'],
                    form.cleaned_data['content']
                ),
                'contacto@correo.com',
                ['contacto@correo.com'],
                reply_to=[form.cleaned_data['email']]
            )
            try:
                email.send()
                messages.add_message(
                    request, messages.SUCCESS, "Mensaje enviado"
                )
            except:
                messages.add_message(
                    request, messages.ERROR, "Error Al enviar mensaje"
                )

            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {'form': form})

