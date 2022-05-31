from django.shortcuts import render, redirect
from .forms import RegisterForm

# Thank you Tech With Tim for guiding me through the User Creation Process Code in this Register App
def register(request):
	if request.method == "POST":
		register_form = RegisterForm(request.POST)
		if register_form.is_valid():
			register_form.save()
			return redirect("/")

	else:
		register_form = RegisterForm()

	context = {"register_form" : register_form}
	return render(request, "register/register.html", context)