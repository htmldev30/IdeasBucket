from django.urls import path
from . import views

urlpatterns = [
	path("", views.home, name="home"),
	path("privacy-policy/", views.privacyPolicy, name="privacyPolicy"),
	path("terms-of-service/", views.termsOfService, name="termsOfService"),
]