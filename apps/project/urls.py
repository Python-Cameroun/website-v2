from django.urls import path
from .views import projects_view, project_view

urlpatterns =[
    path('', projects_view, name = 'projects'),
    path('<slug:slug>/', project_view, name = 'project'),

]