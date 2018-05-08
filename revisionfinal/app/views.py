from django.shortcuts import render
from app.forms import userform,userformother
# Create your views here.
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request,'app/index.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def registration(request):
    registered=False
    if request.method=="POST":
        user_form=userform(data=request.POST)
        additional_form=userformother(data=request.POST)
        if user_form.is_valid() and additional_form.is_valid():
            user=user_form.save()
            user.set_password(user.password)
            user.save()

            additional=additional_form.save(commit=False)
            additional.user=user
            if "image" in request.FILES:
                additional.image=request.FILES["image"]
            additional.save()
            registered=True
        else:
            print(user_form.errors,additional_form.errors)
    else:
        user_form=userform()
        additional_form=userformother()

    return render(request,"app/registration.html",{"registered":registered,"user_form":user_form,"additional_form":additional_form})

def user_login(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse("index"))
            else:
                return HttpResponse("Not active ")
        else:
            return HttpResponse("Incorrect details have been supplied ")
    else:

        return render(request,"app/login.html",{})
