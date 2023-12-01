from django.urls import path
from django.conf.urls.static import static
from app1.views import *



app_name='app1'


urlpatterns = [
    path('',index,name='indexurls'),
    path('dashboard/',dashboard,name='dashboardurls'),
    path('caradd/',caradd,name='caraddurls'),
    path('carmod/',carmod,name='carmod'),
    path('car_added/',car_added,name='car_added'),
    path('carmod_view/',carmod_view,name='carmod_view'),
    path('final_settlement_car/',final_settlement_car,name='final_settlement_car'),
    path('final_settlement_table/',final_settlement_table,name='final_settlement_table'),
]