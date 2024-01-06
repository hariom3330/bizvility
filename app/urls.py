from django.urls import path,include
from app import views
from .import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages


import random
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.urls import path
from django.urls import path
from .views import send_otp, login_with_otp
import uuid

urlpatterns = [
    path('',views.home ,name = 'home'),
    path('signup/', views.signup ,name='signup' ),
    path('login/', views.login, name='login' ),
    path('logout/', views.logout, name='logout'),
    path('ForgetPassword/', views.ForgetPassword, name='ForgetPassword'),
    # path('ChangePassword/<token>/', views.ChangePassword, name ='ChangePassword'),
    path('ChangePassword/<token>/', views.ChangePassword, name='ChangePassword'),
    path('send-otp/', send_otp, name='send_otp'),
    path('login-with-otp/', login_with_otp, name='login_with_otp'),
   
    path('searching/', views.searching, name='searching'),
  
    
 
    # path('edit/', views.edit, name='edit'),
  
    # path('<int:product_id>/review/', views.review, name='review'),s
    path('listing/<int:pk>/review/', views.review, name='review'),
    path('listing/<int:pk>/review/<int:review_id>/delete/', views.delete_review, name='delete_review'),
   
    
    path('fl/<str:pk>',views.fl,name='flifall'),
    path('form',views.form,name='form'),
    # path('searching/', views.searchingView.as_view(), name="searching"),
    path('social-auth/',include('social_django.urls',namespace='social')),
  
    # path('searching/edit/', views.edit, name='edit'),

    
    # path('result/<int:pk>', views.resultview.as_view(), name='result'),
    path('productdetail/<int:pk>', views.ProductDetailView.as_view(), name="productdetail"),
    ##Forget password by email
    path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
    

 ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

 


     

