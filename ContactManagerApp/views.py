"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
from django.template import RequestContext
from datetime import datetime
from ContactManagerApp.models import Contact
from .forms import ContactForm1
def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    context = {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    return render(request,'ContactManagerApp/index.html',context)

def contact(request):
    """Renders the contacts page."""
    assert isinstance(request, HttpRequest)
    lstContacts = Contact.objects.all()
    context = {
            'title' : 'Contact List',
            'message' : '',
            'year' : datetime.now().year,
            'lstContacts' : lstContacts
        }

    return render(request,'ContactManagerApp/contact.html',context)
    

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    context = {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year
        }
    return render(request, 'ContactManagerApp/about.html',context)

def manage_contact(request,contactid):
    """Renders the add edit contact page."""
    assert isinstance(request, HttpRequest)    
    objContact = Contact()
    if request.method == 'GET':
        if contactid != '0':
            objContact = Contact.objects.get(id=int(contactid))
            form = ContactForm1(initial={'id':objContact.id,'firstname': objContact.FirstName,'lastname': objContact.LastName,'email':objContact.Email,'mobileno':objContact.MobileNo })          
        else:
            form = ContactForm1()
    if request.method == 'POST':      
        form = ContactForm1(request.POST)
        if form.is_valid():
            if contactid != '0':      
                objContact.id = int(contactid)     
            objContact.FirstName = request.POST['firstname']
            objContact.LastName = request.POST['lastname']
            objContact.Email = request.POST['email']
            objContact.MobileNo = request.POST['mobileno']
            objContact.save()                           
    return render(request, 'ContactManagerApp/manage_contact.html',{'form':form})   

def delete_contact(request,contactid):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)   
    if request.method == 'GET':
        if contactid:
            Contact.objects.get(id=int(contactid)).delete()
            if request.is_ajax()== True:
                return HttpResponse('Record deleted successfully')

def manage_employee(request):
    context = {
            'title':'Employee',
            'message':'Your Employee Registration page.',
            'year':datetime.now().year
        }
    if request.is_ajax():
         if request.method == 'GET':
             print (request.GET)             
         elif request.method == 'POST':
             print (request.POST['name'])
         return HttpResponse(request.POST['name'] +'Record submitted successfully')
    else:
        return render(request, 'ContactManagerApp/manage_employee.html',context)    
