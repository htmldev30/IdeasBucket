from django.forms import ModelForm
from django import forms
from .models import UserProfile


'''class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ["user_bio"]
		
		widgets = {

			'user_bio' : forms.TextInput(attrs={"placeholder" : "Add Bio"})

		}'''
