from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from . import views



app_name='UMS'


urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

]