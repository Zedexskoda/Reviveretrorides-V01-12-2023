from django.shortcuts import render
from django.shortcuts import render, redirect
# from .forms import CustomUserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from app1.models import *
from app1.forms import *
# from .forms import LoginForm
# Create your views here.
app_name='app1'


def index(request):
    return render(request,"app1/index.html")


def car_added(request):
    all_details = All_Detail.objects.all()
    mod = car_x_mod.objects.all()

    context = {
        'all_details': all_details,
        'mod': mod,
    }
    return render(request,'app1/CARADDED_TABLE.html',context)


def dashboard(request):
    return render(request,'app1/dashboard.html')


def caradd(request):
    if request.method == 'POST':
        form = AllDetailForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('app1:dashboardurls')
        else:
            print(form.errors)
    else:
        form = AllDetailForm()
    cars = Car.objects.all()
    models = Model.objects.all()

    context = {
        'cars': cars,
        'models': models,
        'form': form,
    }

    return render(request,'app1/addcar.html',context)


def carmod(request):
    if request.method == 'POST':
        form = CarXModForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('app1:dashboardurls')  # Replace 'success_url' with the actual URL
    else:
        form = CarXModForm()

    car_details = All_Detail.objects.all()
    works = Work.objects.all()
    context={
        'car_details':car_details,
        'works':works,
        'form':form,
    }
    return render(request, 'app1/carmod.html', context)


def carmod_view(request):
    mod = car_x_mod.objects.all()

    context = {
        'mod': mod,
    }
    return render(request,'app1/CARMOD_VIEW.html',context)


def final_settlement_car(request):
    if request.method == 'POST':
        form = FinalSettlementForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('app1:dashboardurls')  # Replace 'success_url' with the actual URL
    else:
        form = FinalSettlementForm()
    car_details = All_Detail.objects.all()
    works = Work.objects.all()
    context={
        'car_details':car_details,
        'works':works,
        'form':form,
    }
    return render(request,'app1/final_settlement.html',context)


def final_settlement_table(request):
    finalmod = final_settlement.objects.all()

    context = {
        'finalmod': finalmod,
    }
    return render(request,'app1/FINALSETTLEMENT_TABLE.html',context)