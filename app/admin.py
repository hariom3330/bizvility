from django.contrib import admin
from django.contrib import admin
from . models import listing,Enquire,Review,Profile,Category,Phone
from phone_field import PhoneField
from embed_video.admin import AdminVideoMixin



   


# class listingadmin(AdminVideoMixin,admin.ModelAdmin):
#     list_display = ('id','category','name','phone','website','specification','heading','about','youtub','address','open_timing','address_image','background_image','gallery_img1','gallery_img2','gallery_img3','gallery_img4','gallery_img5')
# admin.site.register(listing,listingadmin)
admin.site.register(listing)


 
class Profileadmin(admin.ModelAdmin):
    list_display=('id','user','forget_password_token','create_at','is_verified')
admin.site.register(Profile,Profileadmin)  
class Categoryadmin(admin.ModelAdmin):
    list_display=('name',)
admin.site.register(Category,Categoryadmin) 


class Phoneadmin(admin.ModelAdmin):
    list_display=('phone',)
admin.site.register(Phone,Phoneadmin) 


class Reviewadmin(admin.ModelAdmin):
    list_display = ('id','user','namee','exprince','emaill','review')
admin.site.register(Review,Reviewadmin)  


class Enquireadmin(admin.ModelAdmin):
    list_display = ('id','first_name','last_name','Business_name','Business_categrey','phone','email','address')
admin.site.register(Enquire,Enquireadmin)  
