from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from Post.forms import IdeaForm, CommunityForm
from Post.models import Idea, Communities
# Create your views here.



def home(request, pk=None):

        
	if User.is_authenticated:
		community_form = CommunityForm(request.POST)
		if request.method == "POST":
			community_form = CommunityForm(request.POST, request.FILES)
			if community_form.is_valid():
				community_post_instance = community_form.save(commit=False)
				community_post_instance.user_created_by = request.user
				community_post_instance.save()
				messages.success(request, "Your Community Was Created Successfully")
				return redirect("home")
		else:	
			community_post_instance = CommunityForm()

	if request.method == 'POST':
		idea_form = IdeaForm(request.POST)
		if idea_form.is_valid():
			idea_instance = idea_form.save(commit=False)
			idea_instance.user = request.user
			idea_instance.save()
			messages.success(request, "Your Idea Was Created")
			return redirect("home")
	
	else:
		idea_form = IdeaForm()
	
	# User Profile 
	if pk:
		user = User.objects.get(pk=pk)
	else:
		user = request.user



	# User Ideas
	if not user.is_authenticated:
                return redirect("register")

	ideas = Idea.objects.filter(user=request.user, is_public=False).order_by('-time_posted')
	pub_ideas = Idea.objects.filter(user=request.user,is_public=True).order_by('-time_posted')


	context = {"user":user, "idea_form" : idea_form, "community_form": community_form,
					"ideas" : ideas, 'pub_ideas' : pub_ideas}
	return render(request, "views_gen/home.html", context)


def privacyPolicy(request):
	return render(request, "views_gen/privacy_policy.html")
	
def termsOfService(request):
	return render(request, "views_gen/terms_of_service.html")
