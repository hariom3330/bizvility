from django.shortcuts import render,redirect,HttpResponse
from django.shortcuts import get_object_or_404, render
from django.shortcuts import render
from django.contrib import messages 
from django.contrib.auth.models import User 
from django.http import JsonResponse

import random
from .models import *
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.http import HttpResponse
from phonenumber_field.formfields import PhoneNumberField
import random
from django.core.validators import validate_email
from .models import listing,Enquire,Review,Profile
from .models import  Category
from phone_field import PhoneField
from .recommendation_engine import generate_recommendations
from django.views import View
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User, auth
from .helpers import send_forget_password_mail
from django.contrib.auth import login as auth_login,logout as auth_logout
from django.contrib.auth.decorators import login_required
import uuid


from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required





def home(request):
 return render(request, 'index.html')





def signup(request):
    try:

        if request.method=='POST':
            username= request.POST['username']
            email= request.POST['email']
            password= request.POST['password']
            password2=request.POST['password2']

        
        try:
            if User.objects.filter(username=username).first():
                messages.success(request,"username is taken.")
                return redirect('home')
            
            if User.objects.filter(email=email).first():
                messages.success(request,"email is taken ")
                return redirect('signup')

        # if email==True:
        #     messages.error(request,"this email is already exists")
        #     return redirect('register')
        
            if password!=password2:
                messages.error(request,"password and confirm password did not match please register again")
                return redirect('signup')
            

            user = User.objects.create(username=username, email=email)
            # use for security of the password
            user.set_password(password)
            user.save()
            profile =Profile.objects.create(user=user)
            profile.save()
            return redirect('home')
            
            # messages.success(request,"Your Account Successfullymm Created")
            # return render(request,'signup.html') 
        except Exception as e:
            print(e)
           
    except Exception as e:
        print(e)         

    return render(request,'signup.html')





def login(request):
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
      

        try:
            user = authenticate(username=username, password=password)
        except:
            user = User.objects.filter(username=username, password=password)
            print(user)
        if user is not None:
            auth_login(request, user)
            messages.success(request, f'You are login as using {request.user}')
            return redirect('home')
        else:
            messages.error(request, 'Please enter valid email and password')
            return redirect('signup')

    return render(request,'signup.html') 






def searching(request):
    one = request.GET['query']

    all =listing.objects.filter(keywords__icontains=one) 
    param ={'all':all}
    return render(request, 'listing-search.html',param)  




def fl(request,pk):
        all =listing.objects.filter(keywords__icontains=pk).all() 
    
      
        return render(request, 'listing-search.html',{'all':all})  

     

def logout(request):
	auth_logout(request)
	messages.success(request,"Logout Succesfully")
	return redirect('/')
import uuid


def ChangePassword(request,token):
    context = { }
    try:
        profile = Profile.objects.filter(forget_password_token=token).first()
        context = {'user_id':profile.user.id}

        if request.method =='POST':
            password=request.POST.get('password')
            password2 = request.POST.get('password2')
            user_id = request.POST.get('user_id')
            if user_id is None:
                messages.error(request, 'No user id found')
                return redirect(f'/ChangePassword/{token}/')
            if password != password2:
                messages.error(request, 'both password not same')
                return redirect(f'/ChangePassword/{token}/')    
            user = User.objects.get(id=user_id)
            user.set_password(password)
            user.save()
            return redirect('/login/')

           



       



        
    except Exception as e:
        print(e)

        print(e) 

    return render(request,'reset.html',context)
    


def ForgetPassword(request):
    try:
        if request.method =='POST':
            username = request.POST.get('username')
            if not User.objects.filter(username=username).first():
                messages.error(request, 'No user found with this username ')
                return redirect('/ForgetPassword/')
            user = User.objects.get(username=username)
            print(user.email)
            token = str(uuid.uuid4())
            profile =Profile.objects.get(user=user)
            profile.forget_password_token=token
            profile.save()
            send_forget_password_mail(user.email,token) 
            messages.error(request, 'email is send your mail ')
            return redirect('/ForgetPassword/')
                

    except Exception as e:
        print(e)    
    return render(request,'forget.html')








    # one = request.GET.get('query', None)
    # if one is not None:
    #     return HttpResponse('searching: ' + one)
    # else:
         
    #      return HttpResponse('No search query specified')

#     # print(one)
#     # one = request.POST.get('query', False)
#     all =listing.objects.filter(about__icontains=one) 
# #    all = Show_page.objects.all()
#     param ={'all':all}
#     return render(request, 'Search-Preview.html',param)  






class ProductDetailView(View):
    def get(self,request,pk):
        listings = listing.objects.get(id=pk)
        print(listings)
        reviews = Review.objects.filter(listings=listings)
 

        return render(request, 'listing.html', {'listing':listings,'reviews': reviews})    

def form(request):

    if request.method == 'POST':
        first_name= request.POST['first_name']
        last_name= request.POST['last_name']
        Business_name= request.POST['Business_name']
        Business_categrey= request.POST['Business_categrey']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']
        enquery = Enquire.objects.create(first_name=first_name,last_name=last_name,Business_name=Business_name,Business_categrey=Business_categrey, email=email,phone=phone,address=address)
        enquery.save()
        return render(request, 'index.html')

    return render(request, 'listingform.html')


 



     






# def profile(request):

     
#     return render(request, 'profile.html')
  
# def register(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         name = request.POST.get('name')
#         mobile = request.POST.get('mobile')
        
#         check_user = User.objects.filter(email = email).first()
#         check_profile = Profile.objects.filter(mobile = mobile).first()
        
#         if check_user or check_profile:
#             context = {'message' : 'User already exists' , 'class' : 'danger' }
#             return render(request,'otherpage.html' , context)
            
#         user = User(email = email , first_name = name)
#         user.save()
#         otp = str(random.randint(1000 , 9999))
#         profile = Profile(user = user , mobile=mobile , otp = otp) 
#         profile.save()
#     return render(request,'detail.html')






   
      
def review(request,pk):
  
    if request.method == 'POST':
        user = request.user
        name = request.POST['name']
        # Listing = listing.objects.get(id=id)
        rating= request.POST.get('rating')
        email= request.POST['email']
        comment= request.POST['comment']
        listings = listing.objects.get(pk=pk )
        
         
        enquery = Review.objects.create(listings=listings, user=user,name=name,rating=rating,comment=comment,email=email)
        enquery.save()
        
        # If it's an AJAX request, return a JsonResponse
        return redirect('/')  
    return render(request, 'home.html')

def delete_review(request, pk, review_id):
    # Assuming 'pk' is the listing ID, and 'review_id' is the review ID
    review = get_object_or_404(Review, review_id)

    # Check if the user has permission to delete the review (you can customize this part)
    # For example, you might want to check if the user is the author of the review
    if request.user == review.user:
        review.delete()

        # You might want to add a success message or handle the deletion in a different way
        # messages.success(request, 'Review deleted successfully')

    # Redirect to the listing detail page or any other page as needed
    return redirect('listing_detail', pk=pk)


    




    
def logout(request):
	auth_logout(request)
	messages.success(request,"Logout Succesfully")
	return redirect('/')  
    
    
    
    
    
    
    
    
    
    #     user = request.user
    #     namee = request.POST['namee']
    #     emaill = request.POST['emaill']
    #     exprince = request.POST['exprince']
    #     review = request.POST['review']
    #     enquery = Review.objects.create( user=user,namee=namee,emaill=emaill,exprince=exprince,review=review)
    #     enquery.save()
    #     all =Review.objects.all()
    #     new = {'all':all}
      
    #     return render(request, 'detail.html',new)

    # return render(request, 'home.html')
    





        


# def filterr(request):

#     def get(self,request,pk):
#         listings = listing.objects.get(id=pk)
#         print(listings)
#         return render(request, 'detail.html', {'listing':listings})  
 
# def new(request):

     
#     return render(request, 'new2.html')





# def forget(request):
#     try:
#         if request.method == 'POST':
#             username = request.POST.get('username')

#             if not User.objects.filter(username=username).first():
#                 messages.success(request,"no user name found with this username")   
#                 return render(request, '/singnup/forget')


                     




#     except     
#  return render(request, 'forgetpassword.html')



   
def send_otp(request):
    # Generate and send OTP to the provided phone number (use a third-party SMS service).
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')
        otp = str(random.randint(100000, 999999))  # Generate a random 6-digit OTP
        
        # Implement your OTP sending logic here (e.g., using a third-party SMS service)
        # ...

        # Store the OTP in the session for verification
        request.session['otp'] = otp
        request.session['phone_number'] = phone_number

        return HttpResponse('OTP sent successfully')
    else:
        return render(request, 'send_otp.html')

def login_with_otp(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')
        otp = request.POST.get('otp')

        # Verify OTP
        stored_otp = request.session.get('otp')
        stored_phone_number = request.session.get('phone_number')

        if stored_otp == otp and stored_phone_number == phone_number:
            # OTP is valid, authenticate the user
            user = authenticate(request, username=phone_number, password=otp)

            if user is not None:
                login(request, user)
                messages.success(request, 'Login successful')
                return redirect('home')
            else:
                messages.error(request, 'Invalid OTP')
        else:
            messages.error(request, 'Invalid OTP or phone number')
    else:
        return render(request, 'login_with_otp.html')

 