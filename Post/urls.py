from django.urls import path
from . import views

urlpatterns = [
	path("c/", views.communities, name="communities"),
	path("c/<slug:c_slug>/", views.community_page, name="community"),
]