from django.contrib import admin
from app1.models import *
# Register your models here.


@admin.register(Car)
class Car_admin(admin.ModelAdmin):
    list_display=('id','name',)

@admin.register(Work)
class Car_admin(admin.ModelAdmin):
    list_display=('id','work',)


@admin.register(Model)
class Model_admin(admin.ModelAdmin):
    list_display=('id','models',)

@admin.register(All_Detail)
class Model_admin(admin.ModelAdmin):
    list_display=('registration_no','car','car_model','year','chassis_no','engine_no','owner_name','manufacturing_year','state',)



@admin.register(car_x_mod)
class car_x_modl_admin(admin.ModelAdmin):
    list_display=('car','work','before_work','estimate','remarks',)



@admin.register(final_settlement)
class car_x_modl_admin(admin.ModelAdmin):
    list_display=('car','work','after_work','estimate','Final_cost','remarks')
