
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from Noteable_Budgeting import views as calculator_views

#The main page is calculator/test. This is the gateway.
urlpatterns = [
    url(r'^test/$', calculator_views.formview, name='test'),
]
