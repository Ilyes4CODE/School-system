from django.urls import path
from . import views
urlpatterns = [
    path('',views.authentication,name="auth"),
    path('login',views.authentication_login,name="login_view"),
    path('logout',views.logout_view,name="logout_view"),
    path('prof',views.register_prof,name="prof_registration"),
    #path('Error',views.ErrorAtr,name="error"),
]
