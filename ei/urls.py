from django.urls import path
from ei import views

urlpatterns = [
    path('',views.login1,name="login"),
    path('home',views.home,name="home"),
    path("logout",views.logout1,name="logout"),
    path("signup",views.signup,name="signup"),
    path('second<name>',views.second,name="second"),
    path('drop',views.drop,name="drop"),
    path('detail<id>',views.details,name="detail"),
    path('book<id>',views.book,name="book"),
    path('book1',views.book,name="book1"),
    path('contact',views.contact,name="contact"),
    path('about',views.about,name="about"),
    path('dash',views.dashbord,name="dash"),
    path('pay<id>',views.pay,name="pay"),
    path('delit<id>',views.delete,name="delete"),
    path('payment/<id>',views.payment1,name="payment"),
    path('success',views.success,name="success"),
    path('run-migrations/', views.run_migrations),
    path('create-superuser/', views.create_super_user),

]