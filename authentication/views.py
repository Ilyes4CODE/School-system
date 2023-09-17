from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import Group
from dashboard.models import student,prof
from .forms import register_user,login_user,prof_registration
from django.contrib import messages
from .decorators import *
from .functions import verify
# Create your views here.

def authentication(request):
    form = register_user()
    if request.method == 'POST':
        form = register_user(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='student')
            user.groups.add(group)
            student.objects.create(user=user,name=user)
            message = messages.success(request,'Account Was Created Succesfully For ' + username)
            return redirect('login_view')
    context = {'form': form}

    return render(request,'authentication/authentication.html',context)

def authentication_login(request):
    if request.method == 'POST':
        username = request.POST.get('Username')
        password = request.POST.get('Password')
        user = authenticate(request,username = username, password = password)
        if user.groups.get() == Group.objects.get(name='student'):
            if user is not None:
                login(request,user)
                return redirect('stdash')
        else:
            if user.groups.get() == Group.objects.get(name='prof'):
                if user is not None:
                    login(request,user)
                    return redirect('prdash')
            else:
                if user.groups.get() == Group.objects.get(name='admin'):
                    if user is not None:
                        login(request,user)
                        return redirect('addash')

    return render(request,'authentication/login.html')

def register_prof(request):
    form = prof_registration()
    if request.method == 'POST':
        form = prof_registration(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='prof')
            user.groups.add(group)
            prof.objects.create(user = user,first_name=user)
            messages.success('Prof Account Successfully for' + username)
            return redirect('prof_registration')
    context = {'reg': form}
    return render(request,'authentication/prof.html', context)

def logout_view(request):
    logout(request)
    return redirect('/')


def ErrorAtr(request):
    return render(request,'error/atr.html')
