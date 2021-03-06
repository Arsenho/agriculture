from django.conf.urls import url
from . import views

urlpatterns = [
    url('^farmer_registration$', views.farmer_registration_view, name='farmer_registration'),
    url('^farmer_registration_success$', views.farmer_registration_success_view, name='farmer_registration_success'),
    url('^all_farmers$', views.all_farmers_view, name='all_farmers'),
]
