from django.urls import path, include
from . import views

app_name = "core"

urlpatterns = [
    path('', views.BaseView.as_view(), name='main'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('trener/', include('trener.urls'), name='trener'),
]