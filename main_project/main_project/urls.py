"""main_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from os import name
from django.contrib import admin
from django.urls import path
from calc_app import views
# from signin_app import views
from signin_app.views import SignInView, HomeView, SignUpView, SignOutView, GuesspageView, Guess, MadlibsView, RsppageView
# from calc_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('calcpage/', views.calcPage),
    path('compute/', views.compute),
    path('guesspage/', GuesspageView.as_view(), name='guesspage'),
    path('guess/', Guess.as_view(), name='guess'),
    path('index/', HomeView.as_view(), name='index'),
    path('signIn/', SignInView.as_view(), name='signin'),
    path('signUp/', SignUpView.as_view(), name='signup'),
    path('signout/', SignOutView.as_view(), name='signout'),
    path('rsppage/', RsppageView.as_view(), name='rsppage'),
    path('madlibs/', MadlibsView.as_view(), name='madlibs'),
]
