"""
Definition of urls for ContactManagerProject.
"""
from datetime import datetime
from django.conf.urls import include,url
from ContactManagerApp.forms import BootstrapAuthenticationForm
from ContactManagerApp.views import home,contact,about, manage_contact, delete_contact, manage_employee
from django.contrib.auth.views import login,logout
# Uncomment the next lines to enable the admin:
#from django.conf.urls import include
#from django.contrib import admin
#admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^$', home, name='home'),
    url(r'^contact$', contact, name='contact'),
    url(r'^about', about, name='about'),
    url(r'^employee$', manage_employee, name='employee'),
    url(r'^contact/managecontact/(?P<contactid>\d+)/$', manage_contact, name='managecontact' ),
    url(r'^contact/deletecontact/(?P<contactid>\d+)/$', delete_contact, name='deletecontact' ),
    url(r'^login/$',
        login,
        {
            'template_name': 'ContactManagerApp/login.html',
            'authentication_form': BootstrapAuthenticationForm,
            'extra_context':
            {
                'title':'Log in',
                'year':datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        logout,
        {
            'next_page': '/',
        },
        name='logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include(django.contrib.admindocs.urls)),

    # Uncomment the next line to enable the admin:
    #url(r'^admin/', include(admin.site.urls)),
]
