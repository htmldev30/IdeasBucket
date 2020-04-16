from django.shortcuts import render, get_object_or_404, redirect
from .models import Communities, Idea
from .forms import IdeaForm
# Create your views here.
def communities(request):
	all_communities = Communities.objects.all()

	context = {"all_communities" : all_communities}
	return render(request, "communities_page.html", context)

def community_page(request, c_slug):

	community = get_object_or_404(Communities, community_slug=c_slug)
	comm_ideas = Idea.objects.filter(is_public=True, to_community=community).order_by('-time_posted')

	# Handling Idea Posting 
	if request.method == 'POST':
		idea_form = IdeaForm(request.POST)
		if idea_form.is_valid():
			idea_instance = idea_form.save(commit=False)
			idea_instance.user = request.user
			idea_instance.to_community = community
			idea_instance.is_public = True
			idea_instance.save()
			return redirect("home")
	
	else:
		idea_form = IdeaForm()



	context = {"community": community, "comm_ideas": comm_ideas, "idea_form":idea_form}

	return render(request, "community.html", context)
