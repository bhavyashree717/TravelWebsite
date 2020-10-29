from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Destination
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Creating simple views.
'''
def Register(request):
    #return HttpResponse("This s travel website home page")
    #return render(request,'temp1.html')
  #  fname=request.POST('fname')
    return render(request,'temp2.html')
'''
#Create view for registration page
def Register(request):
    if request.method == 'POST':
        username=request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        user=User.objects.create_user(username=username,email=email,password=password1)
        if password1==password2:
            user.save()
            messages.info(request,"user created")
            return redirect('/')
        else:
            messages.info('passwords not matching')
            return redirect('/')
    else:
        return render(request, 'Register.html')

#creating objects for class Destination
'''def travel(request):
    fname=request.POST['fname']
    #return render(request,'temp1.html',{'fname':fname}
    dest1 = Destination()
    dest1.Destname = 'Bengaluru'
    dest1.desc = 'My city'
    dest1.price = 700
    dest1.img = 'static/images/Bangalore.jpg'
    dest1.offer = False
    #return render(request,'temp1.html',{'dest1':dest1})

    dest2 = Destination()
    dest2.Destname = 'Chennai'
    dest2.desc = 'Beach City'
    dest2.price = 600
    dest2.img = 'static/images/Chennai.jpg'
    dest2.offer = True

    dest3 = Destination()
    dest3.Destname = 'Hyderabad'
    dest3.desc = 'Biryani city'
    dest3.price = 500
    dest3.img = 'static/images/Hyderabad.jpg'
    dest3.offer = False

    dests =[dest1,dest2,dest3]
    return render(request,'temp1.html',{'dests':dests})
'''
#return render(request,'temp1.html',{'dest1':dest1})

#To pass Destination table data to website page (creating objects for class Destination)
def travel(request):
    dests=Destination.objects.all()
    return render(request,"temp1.html",{'dests':dests})
