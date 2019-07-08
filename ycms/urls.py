from django.urls import path
from . import views


urlpatterns = [
    path('', views.Nav3, name='Nav3'),
    path('calendar', views.calendar, name='calendar'),
    path('info', views.info, name='info'),
    path('packagegall', views.packagegall, name='packagegall'),
    path('accounts', views.accounts, name='accounts'),
    path('signup', views.signup, name='signup'),
    path('save_details', views.save_details, name='save_details'),
    path('login', views.login, name='login'),
    path('superUser', views.superUser, name='superUser'),
    path('homeext', views.homeext, name='homeext'),
    path('bootstrap', views.bootstrap, name='bootstrap'),
    path('Nav', views.Nav, name='Nav'),
    path('Nav3', views.Nav3, name='Nav3'),
    path('footer', views.footer, name='footer'),
    path('tour', views.tour, name='tour'),
]
