from django.shortcuts import render,redirect
from.models import Bakery
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def cakes(request):
    return render(request,"cakes.html")

def review(request):
    return render(request,"review.html")

def contact(request):
    data=Bakery.objects.all()
    context={"data":data}
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        message=request.POST.get('message')
        query=Bakery(name=name,email=email,phone=phone,message=message)
        query.save()
        return redirect("/")
    return render(request,"contact.html")

def choc(request):
    return render(request,"choc.html")

def vanila(request):
    return render(request,"vanila.html")

def redvel(request):
    return render(request,"redvel.html")

def bday(request):
    return render(request,"bday.html")

def wedd(request):
    return render(request,"wedd.html")

def mtier(request):
    return render(request,"mtier.html")

def handlesignup(request):
    if request.method=="POST":
        username=request.POST.get("uname")
        email=request.POST.get("email")
        password=request.POST.get("pass1")
        cpassword=request.POST.get("pass2")
        if password!=cpassword:
             messages.info(request,"Password is taken")
             return redirect("/signup")
        try: 
             if User.objects.get(username=username):
                 messages.info(request,"Username is taken")
                 return redirect("/signup")
        except:
             pass
        try:
             if User.objects.get(email=email):
                 return redirect("/")
        except:
             pass
        query=User.objects.create_user(username,email,password)
        query.save()
        print(username,email,password)
        messages.info(request,"Signup success please login")
        return redirect("/login")
    
    return render(request,"signup.html")


def handlelogin(request):
    if request.method=="POST":
        username=request.POST.get('uname')
        password=request.POST.get('pass1')
        myuser=authenticate(username=username,password=password)
        if myuser is not None:
            login(request,myuser)
            return redirect("/")
        else:
            return redirect("/login")
    return render(request,"login.html")

def handlelogout(request):
    logout(request)
    messages.info(request,"Logout Successfully")
    return redirect("/")

