from django.shortcuts import render

# Create your views here.
def deposit(request):
	return render(request,"fundTracker/deposit.html",{})