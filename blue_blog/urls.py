from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from django.views.generic import TemplateView
from accounts.views import UserRegistrationView

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='base.html'),name='home'),
    url(r'^new-user/$', UserRegistrationView.as_view(), name='user_registration'),
]
