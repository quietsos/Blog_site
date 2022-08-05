from multiprocessing.context import ForkContext
from django.shortcuts import render


from .models import Login 
from .models import Signup 

def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')


        logindata = Login()
        logindata.lusername = username
        logindata.lpassword = password

        logindata.save( )



    return render(request,'./auth/login.html', {})




def sign_up(request):


    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')


        signupData = Signup()
        signupData.sfirstname = firstname
        signupData.slastname = lastname
        signupData.semail = email
        signupData.sphone = phone


        signupData.save()
        







    return render(request,'./auth/signup.html', {})
