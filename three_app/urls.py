from django.urls import path
from three_app import views

from django.contrib.auth import views as auth_views
from .views import cart_details, add_to_cart, update_cart, delete_from_cart, beverage_details





urlpatterns = [
    path('home',views.index,name='index.html'),  
    path('',views.indexDemo,name='indexDemo.html'),
    path('about',views.about,name='about.html'),
    path('blog',views.blog,name='blog.html'),
    path('single/<int:pk>/',views.single,name='single.html'),
    
    path('booking', views.booking,name='booking.html'),
    path('contact',views.contact,name='contact.html'),
    path('feature',views.feature,name='feature.html'),
    path('menu',views.menu,name='menu.html'),
    path('team',views.team,name='team.html'),
    path('thanks',views.thanks,name='thanks.html'),
    path('reservation_success',views.reservation_success,name='reservation_success'),
    path('comment',views.comment,name='comment'),
    path('login',views.login_user, name='login'),
    path('logout_user',views.logout_user, name='logout'),
    path('register_user',views.register_user, name='register'),
    path('profile_user',views.profile_user, name='profile'),
    path('edit_profile_user',views.edit_profile, name='edit_profile_user'),
    path('password_reset_complete', views.password_reset_complete, name='password_reset_complete'),
    path('change_password', views.change_password, name='change_password'),
    path('burgers', views.burgers, name='burgers.html'),
    path('beverages', views.beverages, name='beverages.html'),
    path('snacks', views.snacks, name='snacks.html'),
    path('pizza', views.pizza, name='pizza.html'),
    path('pizza/<int:id>/', views.pizza_details, name='pizza_details'),
    path('delete_comment/<int:id>/', views.delete_comment, name='delete_comment'),
    path('burgers/<slug:name>', views.burger_detail, name='name'),
    path('burger_detail', views.burger_detail, name='burger_detail'),
    path('beverage/<int:pk>/', views.beverage_details, name='beverage_details'),
    path('burger/<int:id>/add-to-cart/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_details, name='cart_details'),
    path('add_to_cart/', add_to_cart, name='add_to_cart'),
    path('cart_details', views.cart_details, name='cart_details'),
    path('update_cart', update_cart, name='update_cart'),
    path('delete_from_cart', delete_from_cart, name='delete_from_cart'),
    path('team/<int:pk>/', views.team_member_detail, name='team_member_detail'),
    path('snack_detail/<slug:name>', views.snack_detail, name='name'),
    path('payment', views.payment, name="payment.html"),
    path('payment_order',views.payment_order,name='payment_order'),
    path('success', views.success, name='payment_status'),
  
    


   

  


    # [1] Submit Email Form                             //PasswordResetView.as_view()
    # [2] Email Sent Success Message                    //PasswordResetDoneView.as_view()
    # [3] Link to Password Reset form in Email          //PasswordResetConfirmView.as_view()
    # [4] Password successfullt changed message         //PasswordResetCompleteView.as_view()

    path('reset_password/', 
         auth_views.PasswordResetView.as_view(template_name="password_reset.html"), 
         name="reset_password"),
    path('reset_password_sent/', 
         auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"), 
         name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('reset_password_complete/', 
         auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_complete.html"), 
         name="password_reset_complete"),
]
