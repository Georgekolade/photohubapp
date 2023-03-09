from django.db import models
from django.contrib.auth import get_user_model
import uuid
import datetime

User = get_user_model()

# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    id_user = models.IntegerField()
    bio = models.TextField(blank = True)
    profileimg = models.ImageField(upload_to = 'profile_images', default = False)
    location = models.TextField(blank = True)
    
    def __str__(self):
        return self.user.username
        
    class Meta():
        db_table = 'User Accounts'

class CategoryP(models.Model):
	name = models.CharField(max_length = 100, blank = False, primary_key = True)
	thumbnailp = models.ImageField(upload_to = 'thumbnail/', default = False)

	def __str__(self):
		return self.name

	class Meta():
	 	db_table = 'CPhotos'

class CategoryV(models.Model):
	name = models.CharField(max_length = 100, blank = False, primary_key = True)
	thumbnailv = models.ImageField(upload_to = 'thumbnail/', default = False)

	def __str__(self):
		return self.name

	class Meta():
	 	db_table = 'CVideos'

class P_Post(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4)
    category = models.CharField(max_length = 100)
    user = models.CharField(max_length = 100)
    image = models.ImageField(upload_to = 'post_images')
    caption = models.TextField()
    created_at = models.DateTimeField(default = datetime.datetime.now())

    def __str__(self):
        return self.user
    
    class Meta():
        db_table = 'Picture Posts'

class V_Post(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4)
    category = models.CharField(max_length = 100)
    user = models.CharField(max_length = 100)
    video = models.FileField(upload_to = 'post_videos')
    caption = models.TextField()
    created_at = models.DateTimeField(default = datetime.datetime.now())

    def __str__(self):
        return self.user
    
    class Meta():
        db_table = 'Video Posts'