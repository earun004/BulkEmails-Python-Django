from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView,LogoutView
from . import views

urlpatterns = [

        path('',views.home,name='home'),
        path('vendor/', views.vendor , name='vendor'),
        path('vendor/clean_data/', views.clean_data , name='clean_data'),
        path('clean_data/',views.clean_data, name='clean_data'),
        # path('clean',views.clean,name='clean'),

        # path('<id>/clean_data/clean/',views.clean, name='clean'),

        path('vendor/<id>/clean_data/clean/', views.clean ,name = 'clean'),
        
        
        
       
        path('register/',views.register,name='register'),
        path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
        path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
        
        path('excel_data/',views.excel_data,name='excel_data'),
        path('excel_data/<id>/eview/',views.eview,name='eview'),
        path('excel_data/<id>/eview/add/',views.add,name='add'),
       
       
        path('<id>/add/',views.add,name='add'),
        path('<id>/eview/',views.eview,name='eview'),
        path('<id>/eview/add',views.add,name='add'),
]
