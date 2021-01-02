from django.urls import path
from .views import home_view, about_view, coc_view,contact_view,support_view

urlpatterns = [
    path('',home_view, name='home'),
    path('about/',about_view, name='about'),
    path('code-of-conduct/',coc_view, name='coc'),
    path('contact/',contact_view, name='contact'),
    path('support/',support_view, name='support'),




]
