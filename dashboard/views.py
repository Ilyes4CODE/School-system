from django.shortcuts import render

# Create your views here.
def student_dash(request):
    st = request.user.student.module_set.all()
    context = {
        'st':st
    }
    return render(request, 'accounts/stdash.html' ,context)

def prof_dash(request):
    return render(request, 'accounts/profdash.html')


def admin_dash(request):
    render(request, 'accounts/admin.html')