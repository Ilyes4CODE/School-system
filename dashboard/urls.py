from django.urls import path
from . import views

urlpatterns = [
    path('student_account',views.student_dash,name="stdash"),
    path('prof_account',views.prof_dash,name="prdash"),
    path('administraion',views.admin_dash,name="addash"),
]
