from django.forms import ModelForm
from django import forms
from .models import Idea, Communities


class IdeaForm(forms.ModelForm):
	class Meta:
		model = Idea
		fields = ["idea", "is_public"]

		widgets = {

			'idea' : forms.TextInput(attrs={"placeholder" : "A behive for pandas", "class" : "form-control form-icon-input-left",
										 "id" : "inputLeftIcon1"}),

			'is_public' : forms.CheckboxInput(attrs={"name" : "toggleCheckbox"}),
			
		}

class CommunityForm(forms.ModelForm):
	class Meta:
		model = Communities
		fields = ["community_name", "community_bio"]

		widgets = {

			'community_name' : forms.TextInput(attrs={"placeholder" : "Ideas For Youtube", "class" : "form-control form-icon-input-left",
										 "id" : "inputLeftIcon1"}),

			'community_bio' : forms.TextInput(attrs={"placeholder" : "can't think of posts", "class" : "form-control form-icon-input-left" })
			
		}