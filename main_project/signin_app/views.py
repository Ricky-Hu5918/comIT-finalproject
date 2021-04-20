from typing import ContextManager
from django.http import request, HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, AnonymousUser
# from signin_app.models import Profile
from django.views.generic import View
from django.views.generic.base import TemplateView


# Create your views here.
class HomeView(TemplateView):
    # index page
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

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

class SignOutView(View):
    def get(self, request):
        # print("log out!")
        logout(request)
        return redirect('/index/')


# class GuesspageView(TemplateView):
class GuesspageView(View):
    # guess page
    # template_name = 'guesspage.html'

    # def get_context_data(self, **kwargs):
    #     return super().get_context_data(**kwargs)
    
    def get(self, request):
        return render(request, 'guesspage.html')
    
    def post(self, request):
        pass

class Guess(View):
    def get(self, request):
        pass

    def post(self, request):
        # if request.method == 'POST' and request.POST:
        guess_num = int(request.POST.get('guess_number'))
        random_num = int(request.POST.get('random_number'))
        times = int(request.POST.get('times_value'))

        times = times + 1

        if (guess_num > random_num):
            res = 'You guessed too High!'
        elif (guess_num < random_num):
            res = 'You guessed too Low!'
        else:
            res = 'Congrats! You guessed Right!'
        
        data = {
            'guess_num': guess_num,
            'result': res,
            'times': times
        }

        return JsonResponse(data, json_dumps_params={'ensure_ascii':False})
        # return JsonResponse(data={'data': data}) #it can only pass one data

class RsppageView(View):
    def get(self, request):
        return render(request, 'rsp.html')

class RspView(View):
    def post(self, request):
        pass