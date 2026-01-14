from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from ei.models import Table1,Category,State,Slide,Contact,Details1,payment
from django.core.mail import send_mail
import razorpay 
from django.conf import settings

# Create your views here.

value="None"     
value2="None"
detail="None"
def login1(request):
    e_massage=None
    if(request.method=="POST"):
        un=request.POST['username']
        p=request.POST['password']
        m=authenticate(request,username=un,password=p)
        if m is not None:
            login(request,m)
            return redirect("home")
        else:
            e_massage="Invalid Username and Password"
        
    return render(request,"login2.html",{'e_massage':e_massage})



def signup(requst):
    e_massage=None
    if(requst.method=="POST"):
        un=requst.POST['name']
        p=requst.POST['password1']
        cp=requst.POST['password2']
        if(p!=cp):
            e_massage="Password & Confirm Password not match"
        else:    
            m=User.objects.create_user(username=un,password=p,email=un)
            m.save()
            return redirect("login")
    return render(requst,"sinup1.html",{'e_massage':e_massage})

def logout1(request):
    logout(request)
    return redirect("login")
    
@login_required(login_url="login")        
def home(request):
    obj=Category.objects.all()
    obj1=State.objects.all()
    context={}
    context['data']=obj
    context['data1']=obj1
    return render(request,"home.html",context)

def second(request,name):
    find=['Uttarkhand','Kerala','Himachal Pradesh',"Maharashtra"]
    if(name in find):
        obj=Table1.objects.filter(state=name)
    else:
        obj=Table1.objects.filter(category=name)
    obj2=Slide.objects.filter(name=name)
    context={
        'data':obj,
        'a':name,
        'slide':obj2,
    }
    return render(request,'second.html',context)

def drop(request):
    if(request.method=="POST"):
        value=request.POST['start']
        value2=request.POST['start1']
        context={}
        b=False
        if((value != "None") and (value2 != "None")):
            obj=Table1.objects.filter(category=value,state=value2)
            context['a']=value
            context['b']=value2
        elif(value2 != "None"):
            obj=Table1.objects.filter(state=value2)
            context['a']=value2
            obj2=Slide.objects.filter(name=value2)
            context['slide']=obj2
        else:
            obj=Table1.objects.filter(category=value)
            context['a']=value
            obj2=Slide.objects.filter(name=value)
            context['slide']=obj2
        context['data']=obj
        # value="None"
        # value2="None"
    else:
        return redirect('home')
    return render(request,'second.html',context)


def details(request, id):
    obj2 = get_object_or_404(Table1, id=id)
    obj4 = get_object_or_404(Table1, id=id)
    obj=Table1.objects.filter(id=id)
    a = obj2.district
    obj=Table1.objects.filter(id=id)
    b = obj4.location
    obj1 = Table1.objects.filter(district=a)
    obj3 = Table1.objects.filter(location=b)
    context = {
        'data': obj,
        'data1': obj1,
        'data2':obj3,
        'data3':obj4
    }

    return render(request, 'details.html', context)


def book(request,id):
    if(request.method=="POST"):
        name=request.POST['name']
        mobile=request.POST['mobile']
        email=request.POST['email']
        age=request.POST['age']
        gender=request.POST['gender']
        date=request.POST['date']
        value=request.POST['start3']
        value1=request.POST['start1']
        obj2=Table1.objects.values('district').get(id=id)
        obj4=Table1.objects.values('location').get(id=id)
        obj3=Table1.objects.values('image').get(id=id)
        district=obj2['district']
        location=obj4['location'] 
        obj= payment.objects.values(value1).get(From=value,To=location)
        pay1=obj[value1]
        pay2=obj3['image']
        print(district)
        print(pay1)
        m=Details1.objects.create(
            name=name,
            mobile_no=mobile,
            email=email,
            age=age,
            gender=gender,
            date=date,
            mode=value1,
            prize=pay1,
            From=value,
            To=location,
            image=pay2
        )
        m.save()
        return redirect("dash")
    return render(request,'book.html')

    

def contact(request):
    obj=Slide.objects.filter(name='contact')
    context={
        'slide':obj,
    }
    if(request.method=="POST"): 
        name=request.POST['name']
        mobile_no=request.POST['mobile']
        email=request.POST['email']
        review=request.POST['review']
        obj=Contact.objects.create(name=name,mobile_no=mobile_no,email=email,review=review)
        obj.save()
    return render(request,'contact.html',context)

def about(request):
    return render(request,'about.html')

def dashbord(request):
    m=Details1.objects.all()
    context={
        'data':m
    }
    return render(request,'dashbord.html',context)

def pay(request,id):
    obj=Details1.objects.filter(id=id)
    context={
        'data':obj
    }
    #return HttpResponse("Success")
    return render(request,'pay.html',context)
    # return render(request,'pay.html',context)

def delete(request,id):
    m=Details1.objects.filter(id=id)
    m.delete()
    return redirect('dash')


# def payment1(request,id):
#     client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_SECRET_KEY))
#     prize=Details1.objects.values("prize").get(id=id)
#     p=str(prize['prize'])
#     p1=prize['prize']
#     print(p1)
#     order= Details1.objects.values("email").get(id=id)
#     data = { "amount": p1*100, "currency": "INR", "receipt": p }
#     payment = client.order.create(data=data)
#     print(payment)
#     context={}
#     context['payment']=payment
#     context['p1']=p1*100 
    

#     #return HttpResponse("Success")
#     return render(request,'payment.html',context)

def payment1(request, id):
    details = get_object_or_404(Details1, id=id)

    amount = int(details.prize) * 100   # paisa
    print("AMOUNT:", amount)

    client = razorpay.Client(
        auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_SECRET_KEY)
    )

    data = {
        "amount": amount,
        "currency": "INR",
        "receipt": str(id),
        "payment_capture": 1
    }

    payment = client.order.create(data=data)
    print("ORDER:", payment)

    context = {
        "payment": payment,
        "amount": amount,                     # ✅ IMPORTANT
        "razorpay_key": settings.RAZORPAY_KEY_ID
    }

    return render(request, "payment.html", context)

def success(request):
    
    sub='trip planning Status'
    print(detail)
    msg=f'''Hi Sir/Madam,

    Great news! Your booking is confirmed for your dream getaway! 🌍✈ We're thrilled to be a part of your adventure. Check your inbox for the details, and feel free to reach out if you have any questions.

    

    Safe travels!
    Gajanan Ghule
    Prestige Tours and Travels PVT. LTD.'''

    frm='gajananghule6117@gmail.com'
    u=User.objects.filter(id=request.user.id)
    print(msg)
    to=u[0].email
    print(to)
    send_mail(
        sub,
        msg,
        frm,
        [to],
        fail_silently=False,
    )

    return render(request,'paymentsuccess.html')
#  
from django.core.management import call_command

def run_migrations(request):
    call_command('migrate')
    return HttpResponse("Migrations applied!")

# 
from django.contrib.auth.models import User
from django.http import HttpResponse

def create_super_user(request):
    username = "Gajanan"
    email = "gajananghule6117@gmail.com"
    password = "Gaja2002,@"

    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username=username, email=email, password=password)
        return HttpResponse("Superuser created successfully.")
    else:
        return HttpResponse("Superuser already exists.")
