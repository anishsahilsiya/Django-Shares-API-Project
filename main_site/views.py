from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import UserForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .models import CompanyInfo
from django.core.paginator import Paginator


# Create your views here.
def homepage(request):

	return render(request, "main_site/page1.html")

def signup_page(request):

	if request.method == "POST":

		form = UserForm(request.POST)

		if form.is_valid():

			user = form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f"New User {username} created!")
			login(request, user)
			return redirect(reverse("main_site:homepage"))

		else:
			for msg in form.error_messages:
				messages.error(request, f"{form.error_messages[msg]}")
	else:
		
		form = UserForm()

	return render(request, "main_site/page2.html", context = {"form" : form})

def logout_request(request):

	logout(request)
	messages.success(request, "Logged Out!")
	return redirect("main_site:homepage")

def login_page(request):
	if request.method == "POST":

		form = AuthenticationForm(request, request.POST)

		if form.is_valid():

			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username = username, password = password)

			if user is not None:

				login(request, user)
				messages.success(request, f"User {username} Logged in!")
				return redirect("main_site:homepage")

			else:
				messages.error(request, "Invalid username or password")
		else:
				messages.error(request, "Invalid username or password")
	else:					
		form = AuthenticationForm()
	
	return render(request, "main_site/page3.html", context = {"form" : form})


def market_page(request):

	p = Paginator(CompanyInfo.objects.all(), 10)
	page = request.GET.get('page')
	data = p.get_page(page)

	return render(request, "main_site/page4.html", context = {"data" : data})

def company_page(request, company_id = 1):

	company_details = CompanyInfo.objects.filter(id=company_id)

	return render(request, "main_site/page5.html", context = {"details" : company_details})	