from django.shortcuts import render


from .models import Login 


def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')


        logindata = Login()
        logindata.lusername = username
        logindata.lpassword = password

        logindata.save( )



    return render(request,'./auth/login.html')




def sign_up(request):
    return render(request,'./auth/signup.html', {})
