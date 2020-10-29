from django.shortcuts import render,redirect

from django.contrib.auth.models import User,auth

#Create view for registration page
def Register(request):
    if request.method == 'POST':
     #   print('request method is post')
        username=request.POST('username')
        email = request.POST('email')
        password1 = request.POST('password1')
        password2 = request.POST('password2')
        user = User.objects.create_user({'username':username,'email':email,'password':password1})
       # user = User.objects.create_user(username=username,email=email,password=password1)
        user.save()
        print('user ',+username+ ' created.')
        return redirect('/')
    else:
        print('request method is get')
        return render(request,'Register.html')

