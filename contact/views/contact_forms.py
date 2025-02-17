#from typing import Any, Dict
#from django.http import Http404
#from django.db.models import Q
#from django.core.paginator import Paginator
#from contact.models import Contact
#
from django.shortcuts import render
from contact.forms import ContactForm

# Create your views here.

def create(request):
    if request.method == 'POST':
        context = {
        'form': ContactForm(data=request.POST)
        }
        return render(
               request,
               'contact/create.html',
                context
        )

    context = {
        'form': ContactForm()
    }

    return render(
        request,
        'contact/create.html',
        context
    )