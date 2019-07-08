from django.shortcuts import render
from ycms.forms import *
from django.shortcuts import redirect
from django.http import HttpResponse





def packagegall(request):
    return render(request, 'cm/Packages.html', {})

def Nav(request):
    return render(request, 'cm/landing2.html', {})


def Nav3(request):
    return render(request, 'cm/landing3.html', {})

def tour(request):
    return render(request, 'cm/tour.html', {})



def footer(request):
    return render(request, 'cm/footer.html', {})


def info(request):
    return render(request, 'cm/info_details.html', {})

def bootstrap(request):
	details = event_details.objects.all()
	return render(request, 'cm/bootstrap.html', {'details': details})



def calendar(request):
    return render(request, 'cm/calendar.html', {})

def signup(request):
    return render(request, 'cm/signup.html', {})

def homeext(request):
    return render(request, 'cm/landing.html', {})

def superUser(request):
	print('hahahah')
	details = event_details.objects.all()
	return render(request, 'cm/bootstrap.html', {'details': details})

def save_details(request):
	if request.method == "POST":
		
		data = {
			"eDate": request.POST['eDate'],
			"duration": request.POST['duration'],
			"vAddress": request.POST['vAddress'],
			"eType": request.POST['eType'],
			"fname": request.POST['fname'],
			"lname": request.POST['lname'],
			"email": request.POST['email'],
			"contact": request.POST['contact'],
			"address": request.POST['address']
		}
		form = details_form(data)
		
		if form.is_valid():
		
			form.save()
			print('save')
			return redirect('packagegall')
		else:
			print(form.errors)
			return render(request, 'cm/info_details.html', data)


def accounts(request):
	if request.method == "POST":
		data = {
			"username": request.POST['username'],
			"email": request.POST['email'],
			"password": request.POST['password']			
		}
		form = accounts_form(data)
		
		if form.is_valid():		
			form.save()
			print('save')
			return redirect('home')
		else:
			print(form.errors)
			return HttpResponse(status=400)

def login(request):
	form = login_Form(request.POST)
	if form.is_valid():
		return redirect('home')
	else:
		print(form.errors)
		return HttpResponse(status=400)

           
    



