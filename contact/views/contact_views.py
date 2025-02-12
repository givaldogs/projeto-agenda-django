from django.shortcuts import get_object_or_404,  render, redirect
from django.http import Http404
#from django.http import HttpResponse
from contact.models import Contact
from django.db.models import Q
from django.core.paginator import Paginator

# Create your views here.

def index(request):
    contacts = Contact.objects \
        .filter(show=True)\
        .order_by('-id')
    
    # print(contacts.query)
    #contact_list = Contact.objects.all()
    paginator = Paginator(contacts, 10)  # Show 10 contacts per page.

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'site_title': 'Contatos - ',
    }

    return render(
        request,
        'contact/index.html',
        context
    )

def contact(request, contact_id):
    single_contact = get_object_or_404(
        Contact, pk=contact_id, show = True
        )
    site_title = f'{single_contact.first_name} {single_contact.last_name} - '
    
    context = {
        'contact': single_contact,
        'site_title': site_title,
    }

    return render(
        request,
        'contact/contact.html',
        context
    )

def search(request):

    search_value = request.GET.get('q', '').strip()
    #print(search_value)

    if search_value == '':
        return redirect('contact:index')

    contacts = Contact.objects \
        .filter(show=True)\
        .filter(
            Q(first_name__icontains=search_value) |
            Q(last_name__icontains=search_value)  |
            Q(phone__icontains=search_value)      |
            Q(email__icontains=search_value)
        )\
        .order_by('-id')
    
    # print(contacts.query)
    #contact_list = Contact.objects.all()
    paginator = Paginator(contacts, 10)  # Show 10 contacts per page.

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)


    context = {
        'page_obj': page_obj,
        'site_title': 'Search - ',
        'search_value': search_value,
    }

    return render(
        request,
        'contact/index.html',
        context
    )

