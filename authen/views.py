from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.
def login_(request):
    login_nav=True
    if request.method == 'POST':
        username_data=request.POST['username']
        password_data=request.POST['password']
        u=authenticate(username=username_data,password=password_data)
        print(u)
        if u is not None:
            login(request,u)
            return redirect('cart')
        else:
            messages.add_message(request,messages.ERROR,'login failed !!!put correct credntials')
            return render(request,'login_.html',{'wrong':True,'login_nav':login_nav})
        # try:
        #   user=  User.objects.get(username=username_data)
        #   if password_data == user.password:
        #       login(request,user)
        #   if request.user.is_authenticated:
        #         return redirect('home')
        # except:
        #     return render(request,'login_.html',{'wrong':True})

    return render(request,'login_.html')

def register(request):
    login_nav=True
    if request.method =='POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        email=request.POST['email']
        username=request.POST['username']
        password=request.POST['password']
        try:
            user=User.objects.get(username=username)
            # messages.add_message(request,messages.INFO,'username already taken please use diffent username !!!')
            messages.add_message(request,messages.WARNING,'username already taken please use different username !!!')

        except:
            u=User.objects.create(first_name=firstname,
                                last_name=lastname,
                                email=email,
                                username=username,)
            u.set_password(password)
            u.save()
            return redirect('login_')
    return render(request,'register.html',{'login_nav':login_nav})

def logout_(request):
    logout(request)
    return redirect('login_')

@login_required(login_url='login_')
def profile_(request):
    
    return render(request,'profile_.html')

@login_required(login_url='login_')
def edit_profile(request):
    if request.method == 'POST':
        user = request.user
        user.first_name = request.POST['firstname']
        user.last_name = request.POST['lastname']
        user.email = request.POST['email']
        user.username=request.POST['username']
        user.save()
        return redirect('profile_')
    
    return render(request, 'edit_profile.html', {'user': request.user})

@login_required(login_url='login_')
def update_password(request):
    if request.method == 'POST':
        newpass=request.POST['password']
        print(newpass)

        u=User.objects.get(username=request.user)
        u.set_password(newpass)
        u.save()
        return redirect('logout_')
    return render(request, 'update_password.html')
