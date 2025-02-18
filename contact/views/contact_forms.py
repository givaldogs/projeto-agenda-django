#from typing import Any, Dict
#from django.http import Http404
#from django.db.models import Q
#from django.core.paginator import Paginator
#
from django.shortcuts import render, redirect, get_object_or_404
from contact.forms import ContactForm
from django.urls import reverse
from contact.models import Contact

# Create your views here.

def create(request):
    form_action = reverse('contact:create')
    if request.method == 'POST':
        form = ContactForm(data=request.POST)
        context = {
            'form': form,
            'form_action': form_action,
        }

        if form.is_valid():
            contact = form.save()
            contact.save()
            return redirect('contact:update', contact_id=contact.pk)

        return render(
               request,
               'contact/create.html',
                context
        )

    context = {
        'form': ContactForm(),
        'form_action': form_action,
    }

    return render(
        request,
        'contact/create.html',
        context
    )

def update(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id,
                                 show=True
                                )
    form_action = reverse('contact:update', args=(contact_id,))
    if request.method == 'POST':
        form = ContactForm(data=request.POST, instance=contact)
        context = {
            'form': form,
            'form_action': form_action,
        }

        if form.is_valid():
            contact = form.save()
            contact.save()
            return redirect('contact:update', contact_id=contact.pk)

        return render(
               request,
               'contact/create.html',
                context
        )

    context = {
        'form': ContactForm(instance=contact),
        'form_action': form_action,
    }

    return render(
        request,
        'contact/create.html',
        context
    )