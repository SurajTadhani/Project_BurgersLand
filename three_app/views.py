from django.shortcuts import render,HttpResponse, redirect , get_object_or_404
from .models import *
from .forms import *
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from django.contrib.auth.decorators import login_required
from .models import commetus
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from three_project import settings
import razorpay





# Create your views here.
@login_required(login_url='register')
def index(request):

  if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reservation_success')
  else:
        form = ReservationForm()
  
  bookTable = homebookingitem.objects.all()
  cooking = homecooking.objects.all()
  featureimg = homefeature.objects.all()
  items = homeitems.objects.all()
  foodmenu = homefoodmenu.objects.all()
  ourteam = TeamMember.objects.all()
  testimonial = hometestimonial.objects.all()
  foodblog = homefoodblog.objects.all()
  featuremenu = homefeaturemenu.objects.all()
  featuremenu1 = homefeaturemenu1.objects.all()
  featuremenu2 = homefeaturemenu2.objects.all()
 
  home = {
    'bookTable': bookTable,
    'cooking': cooking,
    'featureimg' : featureimg,
    'items': items,
    'foodmenu' : foodmenu,
    'form': form,
    'ourteam' : ourteam,
    'testimonial':testimonial,
    'foodblog': foodblog,
    'featuremenu' : featuremenu,
    'featuremenu1' : featuremenu1,
    'featuremenu2' : featuremenu2,
  }
  if request.method == 'POST':
    Name = request.POST.get('name')
    Email = request.POST.get('email')
    Subject = request.POST.get('subject')
    Message = request.POST.get('message')
    formData = contactus(name = Name, email = Email, subject = Subject, message = Message)
    formData.save()

    return render(request, 'thank.html')
  
  return render(request, 'index.html',home)


def indexDemo(request):
  bookTable = homebookingitem.objects.all()
  cooking = homecooking.objects.all()
  featureimg = homefeature.objects.all()
  items = homeitems.objects.all()
  foodmenu = homefoodmenu.objects.all()
  ourteam = homeourteam.objects.all()
  testimonial = hometestimonial.objects.all()
  foodblog = homefoodblog.objects.all()
  featuremenu = homefeaturemenu.objects.all()
  featuremenu1 = homefeaturemenu1.objects.all()
  featuremenu2 = homefeaturemenu2.objects.all()

  indexDemo = {
    'bookTable': bookTable,
    'cooking': cooking,
    'featureimg' : featureimg,
    'items': items,
    'foodmenu' : foodmenu,
    
    'ourteam' : ourteam,
    'testimonial':testimonial,
    'foodblog': foodblog,
    'featuremenu' : featuremenu,
    'featuremenu1' : featuremenu1,
    'featuremenu2' : featuremenu2,
  }
  return render(request, 'indexDemo.html',indexDemo)

def reservation_success(request):
  return render(request, 'reservation_success.html')
    
   
    
@login_required(login_url='register')    
def about(request):
  items = homeitems.objects.all()
  cooking = homecooking.objects.all()
 
  about ={
    'items': items,
    'cooking': cooking,
    
  }
  return render(request,'about.html',about)


@login_required(login_url='register')
def blog(request):
  foodblog = homefoodblog.objects.all()
  blog = {
    'foodblog': foodblog,
  }
  return render(request,'blog.html',blog)

@login_required(login_url='register')
def single(request,pk):
  all_blog = get_object_or_404(homefoodblog,pk=pk)
  Data = commetus.objects.all()
  context = {
    'data':Data,
    'all_blog':all_blog,
  }
  if request.method == 'POST':
    Name = request.POST.get('name')
    Email = request.POST.get('email')
    Message = request.POST.get('message')
    formData = commetus(name = Name, email = Email, message = Message)
    formData.save()
    
  return render(request,'single.html',context)




@login_required(login_url='register')
def booking(request):
  if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reservation_success')
  else:
        form = ReservationForm()
 
  if request.method == 'POST':
    Name = request.POST.get('name')
    Email = request.POST.get('email')
    Subject = request.POST.get('subject')
    Message = request.POST.get('message')
    formData = contactus(name = Name, email = Email, subject = Subject, message = Message)
    formData.save()

    return render(request, 'thank.html')
  
  bookTable = homebookingitem.objects.all()
  foodmenu = homefoodmenu.objects.all()
  snackitems = homefoodsnack.objects.all()
  beveragesitems = homefoodbeverages.objects.all()
  pizzaitems = homefoodpizza.objects.all()
  booking ={
    'bookTable': bookTable,
    'foodmenu' : foodmenu,
    'snackitems':snackitems,
    'beveragesitems':beveragesitems,
    'pizzaitems':pizzaitems,
    'form': form,
  }
  return render(request,'booking.html',booking)
@login_required(login_url='register')
def contact(request):
  if request.method == 'POST':
    Name = request.POST.get('name')
    Email = request.POST.get('email')
    Subject = request.POST.get('subject')
    Message = request.POST.get('message')
    formData = contactus(name = Name, email = Email, subject = Subject, message = Message)
    formData.save()

    return render(request, 'thank.html')
  return render(request,'contact.html')
@login_required(login_url='register')
def feature(request):
  featureimg = homefeature.objects.all()
  featuremenu = homefeaturemenu.objects.all()
  featuremenu1 = homefeaturemenu1.objects.all()
  featuremenu2 = homefeaturemenu2.objects.all()
  feature = {
    'featureimg' : featureimg,
    'featuremenu' : featuremenu,
    'featuremenu1' : featuremenu1,
    'featuremenu2' : featuremenu2,
  }
  return render(request,'feature.html',feature)
@login_required(login_url='register')
def menu(request):
  items = homeitems.objects.all()
  foodmenu = homefoodmenu.objects.all()
  snackitems = homefoodsnack.objects.all()
  beveragesitems = homefoodbeverages.objects.all()
  pizzaitems = homefoodpizza.objects.all()
  menu = {
    'items': items,
    'foodmenu' : foodmenu,
    'snackitems' : snackitems,
    'beveragesitems':beveragesitems,
    'pizzaitems':pizzaitems,

  }
  return render(request,'menu.html',menu)

@login_required(login_url='register')
def delete_comment(request, id):
    comment = get_object_or_404(commetus, id=id)
    comment.delete()
    return redirect('single.html')
@login_required(login_url='register')
def team(request):
  ourteam = TeamMember.objects.all()
  team = {
  'ourteam' : ourteam,

  }
  return render(request,'team.html',team)

@login_required(login_url='register')
def team_member_detail(request, pk):
    team_member = get_object_or_404(TeamMember, pk=pk)
    return render(request, 'team_member_detail.html', {'team_member': team_member})




def thanks(request):
  return render(request,'thank.html')
@login_required(login_url='register')
def comment(request):
  Data = commetus.objects.all()
  context = {
    'data':Data,
  }
  return render(request,'comment.html', context)



def password_reset_complete(request):
   return render(request,'password_reset_complete.html')

# def login(request):
#    return render(request,'login.html')


def login_user(request):
    if request.user.is_authenticated:
        return redirect('index.html')
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('index.html')
        else:
            # Return an 'invalid login' error message.
            messages.success(request, ("Invalid Login, Try Again."))
            return redirect('login')
    
    else:
        return render(request,'login.html', {})
    
@login_required
def logout_user(request):
    logout(request)
    messages.success(request, ("Logout Successfull !!"))
    return redirect('login')

def register_user(request):
    if request.user.is_authenticated:
        return redirect('index.html')

    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request, user)
            messages.success(request, ("Registration Successfull !!"))
            return redirect('profile')
    else:
        form = RegisterUserForm()
    return render(request,'signup.html', {'form':form,})


@login_required
def profile_user(request):
    return render(request,'profile.html')

@login_required
def edit_profile(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'editprofile.html', {'form': form})


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            # Log out the user after password change
            logout(request)
            messages.success(request, "Password changed successfully. Please log in with your new password.")
            return redirect('login')  # Redirect to login page
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = PasswordChangeForm(request.user)
    
    return render(request, 'changepassword.html', {'form': form})

@login_required(login_url='register')
def burgers(request):
   burgerItems = Burger.objects.all()
   burgers = {
      'burgerItems' : burgerItems,
   }
   return render(request, 'burgers.html',burgers)
@login_required(login_url='register')
def burger_detail(request, name):
    burger = Burger.objects.all().filter(name=name)
    related_burgers = Burger.objects.all()
    ingredient = Ingredient.objects.all()
    burger_detail ={
       'burger': burger, 
       'ingredient': ingredient,
       'related_burgers': related_burgers,
     }
    return render(request, 'burger_detail.html',  burger_detail)
@login_required(login_url='register')
def snacks(request):
   snackitems = Snack.objects.all()
   snacks = {
      'snackitems' : snackitems
   }
   return render(request, 'snacks.html',snacks)
@login_required(login_url='register')
def snack_detail(request,name):
    snack = Snack.objects.all().filter(name = name)
    related_snacks = Snack.objects.all()
    snack_detail ={
        'snack': snack,
        'related_snacks': related_snacks
    }
    return render(request, 'snack_detail.html', snack_detail)
@login_required(login_url='register')
def beverages(request):
   beveragesitems = foodbeverages.objects.all()
   beverages = {
      'beveragesitems':beveragesitems
   }
   return render(request, 'beverages.html',beverages)
@login_required(login_url='register')
def beverage_details(request, pk):
    beverage = get_object_or_404(Beverage, pk=pk)
    related_beverages = Beverage.objects.filter(category=beverage.category).exclude(pk=pk)[:5]  # Fetch related beverages
    beverage_details = {
       'beverage': beverage,
       'related_beverages': related_beverages
    }
    return render(request, 'beverage_details.html', beverage_details )

   
@login_required(login_url='register')
def pizza(request):
   foodpizzaitems = Pizza.objects.all()
   pizza = {
      "foodpizzaitems" : foodpizzaitems,
   }
   return render(request, 'pizza.html',pizza)
@login_required(login_url='register')
def pizza_details(request,id):
  # pizza = get_object_or_404(Pizza, id=id)
  pizza = Pizza.objects.filter(id=id)
  Pizzanutrition = PizzaNutrition.objects.all().filter(id=id)
  related_pizza = Pizza.objects.all()

  pizza_details = {
       'Pizza': pizza,
       'Pizzanutrition' : Pizzanutrition,
       'related_pizza' : related_pizza
    }
  return render(request, 'pizza_details.html', pizza_details)





@login_required(login_url='register')
@csrf_exempt
def add_to_cart(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        item_name = data.get('name')
        item_price = data.get('price')
        item_quantity = data.get('quantity')
        item_total_price = data.get('totalPrice')
        item_image = data.get('image')

        cart = request.session.get('cart', [])
        cart.append({
            'name': item_name,
            'price': item_price,
            'quantity': item_quantity,
            'total_price': item_total_price,
            'image': item_image
        })
        request.session['cart'] = cart

        return JsonResponse({'success': True}, status=200)
    return JsonResponse({'error': 'Invalid request'}, status=400)

@login_required(login_url='register')
def cart_details(request):
    cart = request.session.get('cart', [])
    return render(request, 'cart_details.html', {'cart_items': cart})


@login_required(login_url='register')
def get_cart_items(request):
    # Example implementation, adjust based on how you store cart items
    cart = request.session.get('cart', [])
    cart_items = []
    for item in cart:
        product = Cart(item['product_id'])  # Replace with actual product fetching logic
        cart_items.append({
            'name': product.name,
            'price': product.price,
            'quantity': item['quantity'],
            'totalPrice': product.price * item['quantity']
        })
    return cart_items

@login_required(login_url='register')
@csrf_exempt
def update_cart(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        cart = request.session.get('cart', [])
        for item in cart:
            if item['name'] == data['name']:
                item['quantity'] = data['quantity']
                item['total_price'] = data['totalPrice']
        request.session['cart'] = cart
        return JsonResponse({'message': 'Cart updated successfully!'})
    return JsonResponse({'error': 'Invalid request'}, status=400)




@login_required(login_url='register')
@csrf_exempt
def delete_from_cart(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name')
        
        cart = request.session.get('cart', [])
        
        cart = [item for item in cart if item['name'] != name]
        
        request.session['cart'] = cart
        
        return JsonResponse({'success': True, 'message': 'Item removed from cart!'})
    
    return JsonResponse({'success': False, 'message': 'Invalid request method.'})




@login_required(login_url='register')
def payment_order(request):
  total_price = request.GET.get('total', 0)
  error_message = None
  if request.method == 'POST':
        name = request.POST.get('name')
        number = request.POST.get('number')
        email = request.POST.get('email')
        amt = request.POST.get('amount')
        amount = int(amt)
     
     
        client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_SECRET))

        razorpay_payment = client.order.create(dict(amount=(int(amount*100)), currency='INR'))
        order_id = razorpay_payment['id']
    
        book = Booking.objects.create(
            name=name,
            number=number,
            email = email,
            amount = amount,
            order_id = order_id
        )
        book.save()
        razorpay_payment['name'] = name
        razorpay_payment['amount']= amount
        razorpay_payment['order_id'] = order_id
        form = Booking(request.POST or None)
        return render(request, 'payment_order.html', {'razorpay_payment': razorpay_payment})
  form = Booking()
  return render(request,'payment_order.html', {'form': form, 'error_message':error_message,'total_price':total_price})

def payment(request):
    return render(request,"payment.html")

@login_required(login_url='register')
def success(request):
    response = request.POST

    # Extract necessary parameters from the POST request
    params_dict = {
        'razorpay_order_id': response.get('razorpay_order_id'),
        'razorpay_payment_id': response.get('razorpay_payment_id'),
        'razorpay_signature': response.get('razorpay_signature'),
    }

    # Initialize Razorpay client
    client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_SECRET))

    try:
        # Verify the payment signature to confirm the transaction is valid
        status = client.utility.verify_payment_signature(params_dict)

        # Retrieve the booking object using the Razorpay order ID
        razorpay_save = Booking.objects.get(order_id=params_dict['razorpay_order_id'])

        # Update the booking object with the payment ID and mark it as paid
        razorpay_save.razorpay_payment_id = params_dict['razorpay_payment_id']
        razorpay_save.paid = True
        razorpay_save.save()

        # If the payment is successfully marked as paid, clear the user's cart
        if razorpay_save.paid:
           
            if 'cart' in request.session:
              del request.session['cart']
             

            # Send a confirmation email to the user
            email = razorpay_save.email
            amount = razorpay_save.amount
            client_name = razorpay_save.name

            subject = 'Payment Successful'
            message = (
                f"Subject: Payment Confirmation for Your Online Order\n\n"
                f"Dear {client_name},\n\n"
                f"We are pleased to inform you that your payment for the recent online order has been successfully processed. "
                f"Thank you for choosing us and trusting our services!\n\n"
                f"Order Summary:\n"
                f"Payment Amount: {amount}\n\n"
                f"If you have any questions or need further assistance, please don't hesitate to reach out.\n\n"
                f"Thank you once again for choosing us. We look forward to serving you in the future!\n\n"
                f"Best regards,\n"
                f"Your Model Team"
            )

            sender_email = settings.EMAIL_HOST_USER
            recipient_email = [email]  # Convert to list if needed

            send_mail(subject, message, sender_email, recipient_email, fail_silently=False)

            # Render the success page with a success status
            return render(request, 'success.html', {'status': True})

    except Exception as e:
        # Handle exceptions, for example, logging the error
        print(f"Error occurred: {str(e)}")
    
    # Render the success page with a failure status if something goes wrong
    return render(request, 'success.html', {'status': False})
