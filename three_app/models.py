from django.db import models

from django.contrib.auth.models import User
import datetime




class chooseUs(models.Model):
  service_icon = models.CharField(max_length=50)
  service_title = models.CharField(max_length=100)
  service_des = models.TextField()

# Create your models here.

class homebookingitem(models.Model):
 
  name = models.CharField(max_length=100,null=True)
  heading = models.CharField(max_length=100,null=True)
  content = models.TextField()
  content1 = models.TextField()


class homefeaturemenu(models.Model):
  name = models.CharField(max_length=100)
  header = models.CharField(max_length=100)
  content = models.TextField()

class homefeaturemenu1(models.Model):
  name = models.CharField(max_length=100)
  header = models.CharField(max_length=100)
  content = models.TextField()

class homefeaturemenu2(models.Model):
  name = models.CharField(max_length=100)
  header = models.CharField(max_length=100)
  content = models.TextField()

class homecooking(models.Model):
  image = models.ImageField(upload_to='images/')
  name = models.CharField(max_length=100,null=True)
  header = models.CharField(max_length=100,null=True)  
  content = models.TextField()
  content1 = models.TextField()
  btn = models.CharField(max_length=100,null=True)


class homefeature(models.Model):
  img = models.ImageField(upload_to='images/')


class homeitems(models.Model):
  classname = models.CharField(max_length=100)
  header = models.CharField(max_length=100) 
  content = models.TextField()
  btn = models.CharField(max_length=100)

class homefoodmenu(models.Model):
  image = models.ImageField(upload_to='images/')
  header = models.CharField(max_length=100,null=True)
  content = models.TextField()  
  price = models.CharField(max_length=100,null=True)  



class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Burger(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to='burger_images/', null=True, blank=True)
    calories = models.IntegerField()
    protein = models.DecimalField(max_digits=5, decimal_places=2)
    fat = models.DecimalField(max_digits=5, decimal_places=2)
    carbs = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.CharField(max_length=50, default='burger')

    def __str__(self):
        return self.name  
    
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    burger = models.ForeignKey(Burger, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total_price = models.DecimalField(max_digits=6, decimal_places=2)

    # def __str__(self):
    #     return f"{self.user.username}'s cart"    
    def __str__(self):
        return f"{self.user.username}'s cart - {self.quantity} x {self.burger.name}"
# burger items end 
#  snack items start
class homefoodsnack(models.Model):
  image = models.ImageField(upload_to='images/')
  header = models.CharField(max_length=100,null=True)
  content = models.TextField()  
  price = models.CharField(max_length=100,null=True) 



class SnackIngredient(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name  

class Nutrition(models.Model):
    calories = models.IntegerField()
    fats = models.DecimalField(max_digits=5, decimal_places=2)
    proteins = models.DecimalField(max_digits=5, decimal_places=2)
    carbs = models.DecimalField(max_digits=5, decimal_places=2)
    vitamins = models.TextField()
    minerals = models.TextField()    

class Snack(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='snack_images/')
    nutrition = models.OneToOneField(Nutrition, on_delete=models.CASCADE)
    availability = models.CharField(max_length=255)  
    category = models.CharField(max_length=50, default='snack') 



    def __str__(self):
        return f'Review of {self.name}'


# snack items end 
# beverage items start

class homefoodbeverages(models.Model):
  header = models.CharField(max_length=100,null=True)
  image = models.ImageField(upload_to='images/')
  content = models.TextField()  
  price = models.CharField(max_length=100,null=True)

class foodbeverages(models.Model):
  header = models.CharField(max_length=100,null=True)
  image = models.ImageField(upload_to='images/')
  content = models.TextField()  
  price = models.CharField(max_length=100,null=True)
  btn = models.CharField(max_length= 20)

class Beverage(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='beverages/')
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100)
    # Add any other fields as required

    def __str__(self):
        return self.name  
     


# beverage items end


#  pizza items start

class homefoodpizza(models.Model):
  header = models.CharField(max_length=100,null=True)
  image = models.ImageField(upload_to='images/')
  content = models.TextField()  
  price = models.CharField(max_length=100,null=True) 

class foodpizza(models.Model):
  name = models.CharField(max_length=100,null=True)
  image = models.ImageField(upload_to='images/')
  content = models.TextField()  
  price = models.CharField(max_length=100,null=True) 
  btn = models.CharField(max_length= 20)   



class PizzaNutrition(models.Model):
    calories = models.IntegerField()
    fat = models.CharField(max_length=20)
    carbohydrates = models.CharField(max_length=20)
    protein = models.CharField(max_length=20)

  

class Pizza(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    ingredients = models.TextField()
    nutrition = models.OneToOneField(PizzaNutrition, on_delete=models.CASCADE)
    size_options = models.JSONField()
    customization_options = models.JSONField()
    price = models.DecimalField(max_digits=10, decimal_places=2) 
    image = models.ImageField(upload_to='pizza_images/')
    availability = models.CharField(max_length=100)
 
     


#  pizza items end

class Reservation(models.Model):
    GUEST_CHOICES = [
        (1, '1 Guest'),
        (2, '2 Guests'),
        (3, '3 Guests'),
        (4, '4 Guests'),
        (5, '5 Guests'),
    ]
    
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile_number = models.CharField(max_length=15)
    date = models.DateField()
    time = models.TimeField()
    guest_count = models.IntegerField(choices=GUEST_CHOICES)

    def __str__(self):
        return f"Reservation for {self.name} on {self.date} at {self.time}"


class contactus(models.Model):
  name = models.CharField(max_length=100)
  email = models.EmailField()
  subject = models.CharField(max_length=200)
  message = models.TextField()  


class homeourteam(models.Model):
  image = models.ImageField(upload_to='images/')
  name = models.CharField(max_length=100)
  position = models.CharField(max_length=100)

class hometestimonial(models.Model):
  image = models.ImageField(upload_to='images/')
  content = models.TextField()
  name = models.CharField(max_length=100)
  position = models.CharField(max_length=100)

class homefoodblog(models.Model):
  name = models.CharField(max_length=200)
  image = models.ImageField(upload_to='images/')
  username = models.CharField(max_length=100)
  category = models.CharField(max_length=100)
  message = models.CharField(max_length=100)
  content = models.TextField()
 
  btn = models.CharField(max_length=100)

 

class commetus(models.Model):
  name = models.CharField(max_length=100)
  email = models.EmailField()
  date = models.DateTimeField(default=datetime.datetime.now,blank=True)
  message = models.TextField()  



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,default=1)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    bio = models.TextField()
    email = models.EmailField()
    birthdate = models.DateField(blank=True, null=True)
    contact = models.CharField(max_length=10)
    gender = models.CharField(max_length=20)
    address = models.TextField()

    def str(self): 
        return f"{self.fname,self.lname,self.email}"
    

class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    biography = models.TextField()
    skills = models.TextField()
    experience = models.TextField()
    achievements = models.TextField()
    profile_picture = models.ImageField(upload_to='team_pictures/')
    twitter_url = models.URLField(blank=True, null=True)
    facebook_url = models.URLField(blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)
    instagram_url = models.URLField(blank=True, null=True)
    contact_email = models.EmailField(blank=True, null=True)
    personal_interests = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    

class Booking(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    number =models.CharField(max_length=10,null=True)
    email = models.EmailField()
    amount = models.PositiveIntegerField(default=0)
    order_id = models.CharField(max_length=100, blank=True)
    paid = models.BooleanField(default=False)
    razorpay_payment_id = models.CharField(max_length=100, blank=True)
 
    def __str__(self):
        if self.paid == True:
            return self.name + " paid"
        else:
            return self.name + " not paid"    
        

           
       
    

 


 