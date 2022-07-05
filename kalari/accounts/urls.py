from django.urls import path
from.views import *
urlpatterns = [

path('',home,name='index'),
path('signup/mykalari/',signup_mykalari,name='account_signup_mykalari'),
path('signup/users/',signup_users,name='account.signup_users'),
path('login/', login_view, name='account_login'),
path('logout/', logout_view, name='account_logout'),
]