from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import math
from django.db.models.signals import pre_save
from django.utils.text import slugify
# Create your models here.

class Communities(models.Model):
    user_created_by = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name="User")
    community_name = models.CharField(max_length=25, null=True)
    community_bio  = models.CharField(max_length=100,null=True)
    community_image_icon = models.FileField(upload_to="community_icons", null=True, 
                                            default='/community_icons/default_community_icon.jpg')
    community_created_time = models.DateTimeField(auto_now_add=True)
    community_slug = models.SlugField(max_length=40, unique=True)

    class Meta:
        verbose_name_plural = "Communities"

    def __str__(self):
        return self.community_name

def pre_save_post_receiver(sender, instance, *args, **kwargs):
    community_slug = slugify(instance.community_name)
    exists = Communities.objects.filter(community_slug=community_slug).exists()
    if exists:
        community_slug = "%s_%s" %(community_slug, instance.id)

    instance.community_slug = community_slug


pre_save.connect(pre_save_post_receiver, sender=Communities)

class Idea(models.Model):
	user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
	idea = models.CharField(max_length=25, null=True)
	is_public = models.BooleanField(default=False)
	to_community = models.ForeignKey(Communities, null=True, on_delete=models.CASCADE)
	
	time_posted = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.idea

	def timesince(self):
		now = timezone.now()

		time_diff = now - self.time_posted

		if time_diff.days == 0 and time_diff.seconds >= 0 and time_diff.seconds < 60:
			seconds=time_diff.seconds

			if seconds < 1:
					return " seconds ago"

		if time_diff.days == 0 and time_diff.seconds >= 60 and time_diff.seconds < 3600:
			minutes=math.floor(time_diff.seconds/60)

			if minutes == 1:
				return str(minutes) + "  minute ago"
			else:
				return str(minutes) + " minutes ago"

		if time_diff.days == 0 and time_diff.seconds > 3600 and time_diff.seconds < 86400:
			hours = math.floor(time_diff.seconds/3600)

			if hours == 1:
				return str(hours) + " hour ago"
			else:
				return str(hours) + " hours ago"

		if time_diff.days >= 30 and time_diff.days < 365:
			months = math.floor(time_diff.days/30)

			if months == 1:
				return str(months) + " month ago"

			else:
				return str(months) + " months ago"


		if time_diff.days >= 365:
			years = math.floor(time_diff.days/365)

			if years == 1:
				return str(years) + " year ago"

			else:
				return str(years) + " years ago" 