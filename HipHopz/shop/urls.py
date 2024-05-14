from django.contrib.auth.urls import path
from . import views

app_name='shop'

urlpatterns=[
    path('',views.Home,name='home'),
    path('register/',views.U_register,name='register'),
    path('login/', views.U_login, name='login'),
    path('logout/', views.U_logout, name='logout'),
    path('sub_cate/<int:p>',views.Sub_cate,name='category'),
    path('items/<int:p>', views.Items, name='items'),
    path('details/<int:p>',views.Details,name='details')

]