from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_func):
    def wrapper(request):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request)
    
    return wrapper

def allowed_user(allowed_user = []):
    def decorator(func):
        def wrapper(request):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_user :
                return func(request)
            else:
                return HttpResponse('You Are Not Authorized To Access To This Page')

        return wrapper
    return decorator

def admin_only(func):
    def wrapper(request):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
        if group == 'customer':
            return redirect('user')
        
        if group == 'admin':
            return func(request)
        
    return wrapper