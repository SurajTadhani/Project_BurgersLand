from django.contrib import admin
from .models import *
from django.contrib import admin
from .models import Burger, Ingredient



# Register your models here.



class chooseUsAdmin(admin.ModelAdmin):
  list_display =('service_title','service_icon','service_des')
admin.site.register(chooseUs, chooseUsAdmin) 


class homebookingitemforadmin(admin.ModelAdmin):
  list_display =["name","heading","content","content1"]
admin.site.register(homebookingitem, homebookingitemforadmin)  


class homecookingforadmin(admin.ModelAdmin):
  list_display =["name","image","header","content","content1","btn"]
admin.site.register(homecooking, homecookingforadmin)  

class homefeatureforadmin(admin.ModelAdmin):
  list_display = ["img"]
admin.site.register(homefeature, homefeatureforadmin)  

class homeitemsforadmin(admin.ModelAdmin):
  list_display = ["classname","header", "content","btn"]
admin.site.register(homeitems,homeitemsforadmin) 


class homefoodmenuforadmin(admin.ModelAdmin):
  list_display = ["header","image","content","price"]
admin.site.register(homefoodmenu,homefoodmenuforadmin) 



class Ingredientforadmin(admin.ModelAdmin):
  list_display = ["name","description"]
admin.site.register(Ingredient,Ingredientforadmin)  

class Burgerforadmin(admin.ModelAdmin):
  list_display = ["name","description","price","image","calories","protein","fat","carbs","category"] 
admin.site.register(Burger,Burgerforadmin)


class SnackIngredientforadmin(admin.ModelAdmin):
  list_display = ["name"]
admin.site.register(SnackIngredient,SnackIngredientforadmin)  

class Nutritionforadmin(admin.ModelAdmin):
  list_display = ['calories','fats','proteins','carbs','vitamins','minerals']
admin.site.register(Nutrition,Nutritionforadmin)  

class Snackforadmin(admin.ModelAdmin):
  list_display = ["name","description","price","image","nutrition","availability","category"] 
admin.site.register(Snack,Snackforadmin)

 




class homefoodsnackforadmin(admin.ModelAdmin):
  list_display = ["header","image","content","price"]
admin.site.register(homefoodsnack,homefoodsnackforadmin)

# class foodsnackitemsforadmin(admin.ModelAdmin):
#   list_display = ["title","image","price","content","btn"]
# admin.site.register(foodsnackitems,foodsnackitemsforadmin) 


class homefoodbeveragesforadmin(admin.ModelAdmin):
  list_display = ["header","image","content","price"]
admin.site.register(homefoodbeverages,homefoodbeveragesforadmin)

class foodbeveragesforadmin(admin.ModelAdmin):
  list_display = ["header","image","content","price","btn"]
admin.site.register(foodbeverages,foodbeveragesforadmin)

class Beverageforadmin(admin.ModelAdmin):
  list_display = ["name","image","description","price","category"]
admin.site.register(Beverage,Beverageforadmin)

class homefoodpizzaforadmin(admin.ModelAdmin):
  list_display = ["header","image","content","price"]
admin.site.register(homefoodpizza,homefoodpizzaforadmin)

class foodpizzaforadmin(admin.ModelAdmin):
  list_display = ["name","image","content","price","btn"]
admin.site.register(foodpizza,foodpizzaforadmin)

class PizzaNutritionforadmin(admin.ModelAdmin):
  list_display = ["calories","fat","carbohydrates","protein"]
admin.site.register(PizzaNutrition,PizzaNutritionforadmin)

class Pizzaforadmin(admin.ModelAdmin):
  list_display = ["name","description","ingredients","nutrition","size_options","customization_options","price","image","availability"]
admin.site.register(Pizza,Pizzaforadmin)  

class Reservationforadmin(admin.ModelAdmin):
  list_display = ["name","email","mobile_number","date","time","guest_count"]
admin.site.register(Reservation, Reservationforadmin)  



class contactusforadmin(admin.ModelAdmin):
  list_display = ["name","email","subject","message"]
admin.site.register(contactus,contactusforadmin)   


class homeourteamforadmin(admin.ModelAdmin):
  list_display = ["name","image","position"]
admin.site.register(homeourteam,homeourteamforadmin)  


class hometestimonialforadmin(admin.ModelAdmin):
  list_display = ["name","image","content","position"]
admin.site.register(hometestimonial,hometestimonialforadmin)


class homefoodblogforadmin(admin.ModelAdmin):
  list_display = ["name","image","username","category","message","content","btn"]
admin.site.register(homefoodblog,homefoodblogforadmin)


class homefeaturemenuforadmin(admin.ModelAdmin):
  list_display = ["name","header","content"]
admin.site.register(homefeaturemenu,homefeaturemenuforadmin)  

class homefeaturemenuforadmin1(admin.ModelAdmin):
  list_display = ["name","header","content"]
admin.site.register(homefeaturemenu1,homefeaturemenuforadmin1) 

class homefeaturemenuforadmin2(admin.ModelAdmin):
  list_display = ["name","header","content"]
admin.site.register(homefeaturemenu2,homefeaturemenuforadmin2)  


class commetusforadmin(admin.ModelAdmin):
  list_display = ["name","email","date","message"]
admin.site.register(commetus,commetusforadmin) 


class TeamMemberforadmin(admin.ModelAdmin):
  list_display = ["name","position","biography","skills","experience","achievements","profile_picture","twitter_url","facebook_url","linkedin_url","instagram_url","contact_email","personal_interests"]
admin.site.register(TeamMember,TeamMemberforadmin)



class Bookingforadmin(admin.ModelAdmin):
  list_display = ['name','email','number','amount','order_id','paid','razorpay_payment_id']
admin.site.register(Booking,Bookingforadmin) 