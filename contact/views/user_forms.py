#
from django.shortcuts import render, redirect
from contact.forms import RegisterForm
from django.contrib import messages
# from django.urls import reverse
# from contact.models import Contact

# Create your views here.

def register(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuário registrado')
            return redirect('contact:index')

    return render(
            request,
            'contact/register.html',
            {
                'form': form
            }
        )

   