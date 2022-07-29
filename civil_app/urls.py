from . import views
from django.urls import path

urlpatterns = [
   
   path('',views.homepage,name='homepage'),
   path('civil_work',views.civil_work,name='civil_work'),

]