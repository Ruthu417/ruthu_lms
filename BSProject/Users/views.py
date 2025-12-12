from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def register(req):
	form=UserCreationForm()
	if req.method=="POST":
		form=UserCreationForm(req.POST)
		if form.is_valid():
			form.save()
			return redirect('register')
	return render(req,'users/register.html',{'form':form})
