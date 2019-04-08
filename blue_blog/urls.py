from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView

from accounts.views import UserRegistrationView

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='base.html'),name='home'),
    url(r'^new-user/$', UserRegistrationView.as_view(), name='user_registration'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    url(r'^logout/$', LogoutView.as_view(), {'next_page':'/login/'}, name='logout'),
]
