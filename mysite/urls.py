from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from Noteable_Budgeting import views as calculator_views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^calculator/test/$', calculator_views.formview, name='test'),
]
