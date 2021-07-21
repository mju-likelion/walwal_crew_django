from os import name
from django.contrib import admin
from django.urls import path
import myapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', myapp.views.main, name='main'),
    path('aboutus/', myapp.views.aboutus, name='aboutus'),
    path('adoption/', myapp.views.adoption, name='adoption'),
    path('passage/', myapp.views.passage, name='passage'),
    path('failure/', myapp.views.failure, name='failure'),
]
