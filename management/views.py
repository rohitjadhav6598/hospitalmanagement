from django.shortcuts import render
from .models import Patient
from django.contrib.auth.decorators import login_required



patients=[
	{
		'Name': 'Akshay',
		'Age':22,
		'DoA':'2/2/2020',
		'Type':'Full',
		'Address':'Pune'
	},
	{
		'Name': 'Rajesh',
		'Age':50,
		'DoA':'2/2/2020',
		'Type':'Full',
		'Address':'Pune'
	}
]

@login_required
def home(request):
	return render(request, 'management/home.html')

@login_required
def list(request):
	context={
		'patients':Patient.objects.all()
	}
	return render(request, 'management/list.html', context)