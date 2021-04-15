from typing import ContextManager
from django.http import request, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, AnonymousUser
# from signin_app.models import Profile
from django.views.generic import View
from django.views.generic.base import TemplateView


# Create your views here.
def home(request):
    return render(request, 'index.html')

class HomeView(TemplateView):
    # index page
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

def signin(request):
    if request.method == 'POST' and request.POST:
        data = request.POST
        username = data.get('username')
        password = data.get('password')
        n = authenticate(username=username, password=password)
        if n:  #log in successfully, return to home page
            login(request, user=n)
            return redirect('/index/')
    #log in failed, redirect to signIn page
    return render(request, 'signIn.html')

class SignInView(View):
    def get(self, request):
        # print("signInView get method! \n")
        return render(request, 'signIn.html')

    def post(self, request):
        if request.POST:
            data = request.POST
            username = data.get('username')
            password = data.get('password')
            n = authenticate(username=username, password=password)
            if n:  #log in successfully, return to home page
                login(request, user=n)
                return redirect('/index/')
        
        #log in failed or POST == NULL, redirect to signIn page
        return render(request, 'signIn.html')

def signup(request):
    if request.method == 'POST' and request.POST:
        data = request.POST
        username = data.get("username")
        email = data.get("email")
        password = data.get("password")

        u = User.objects.filter(username=username).first()
        if u:  #illeagl name
            info = 'This username has been registered!'
            return render(request, 'Error.html', {'info': info})
        else: #success
            #cannot use User.objects.create(), because it will create the password without encryption
            User.objects.create_user(username=username, password=password, email=email)
            #redirect to signin page
            return HttpResponseRedirect('/signIn/')
        
    #register fail
    return render(request, 'signUp.html')

class SignUpView(View):
    def get(self, request):
        return render(request, 'signUp.html')
    
    def post(self, request):
        if request.POST:
            data = request.POST
            username = data.get("username")
            email = data.get("email")
            password = data.get("password")

            u = User.objects.filter(username=username).first()
            if u:  #illeagl name
                info = 'This username has been registered!'
                return render(request, 'Error.html', {'info': info})
            else: #success
                #cannot use User.objects.create(), because it will create the password without encryption
                User.objects.create_user(username=username, password=password, email=email)
                #redirect to signin page
                return HttpResponseRedirect('/signIn/')
        
        #register fail
        return render(request, 'signUp.html')

def signout(request):
    logout(request)
    return redirect('/index/')

class SignOutView(View):
    def get(self, request):
        # print("log out!")
        logout(request)
        return redirect('/index/')


