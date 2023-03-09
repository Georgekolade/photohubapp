from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Profile, P_Post, V_Post, CategoryP, CategoryV
from .form import PhotoForms, VideoForms, CPForms, CVForms
from PIL import Image

# Create your views here.
def register(request):
	if request.method == 'POST':
		username = request.POST['username']
		email = request.POST['email']
		password = request.POST['pass']
		cpass = request.POST['cpass']

		if password == cpass:
			if User.objects.filter(email=email).exists():
				messages.info(request, 'Email Taken')
				return redirect('register')
			elif User.objects.filter(username=username).exists():
				messages.info(request, 'Username Taken')
				return redirect('register')
			else:
				user = User.objects.create_user(username=username, email=email, password=password)
				user.save()
				
				user_model = User.objects.get(username=username)
				new_profile = Profile.objects.create(user=user_model, id_user=user_model.id)
				new_profile.save()
				return redirect('login')
		else:
			messages.info(request, 'Password Not Matching')
			return redirect('register')
	else:
		return render(request, 'register.html')

def login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		user = auth.authenticate(username=username, password=password)

		if user is not None:
			auth.login(request, user)
			return redirect('profile')
		else:
			messages.info(request, 'No account with username / password')
			return redirect('login')
	else:
		return render(request, 'login.html')

@login_required(login_url='login')
def logout(request):
	auth.logout(request)
	return redirect('login')

@login_required(login_url='login')
def profile(request):
    user_profile = Profile.objects.get(user = request.user)
    
    if request.method == "POST":
        if request.FILES.get('image') == None:
            image = user_profile.profileimg
            bio = request.POST['bio']
            location = request.POST['location']

            user_profile.profileimg = image
            user_profile.bio = bio
            user_profile.location = location
            user_profile.save()
        elif request.FILES.get('image') != None:
            image = request.FILES.get('image')
            bio = request.POST['bio']
            location = request.POST['location']

            user_profile.profileimg = image
            user_profile.bio = bio
            user_profile.location = location
            user_profile.save()

            return redirect('profile')

        else:
            pass

    context = {"user_profile" : user_profile}
    return render(request, 'profile.html', context)

@login_required(login_url='login')
def upic(request):
	pics = CategoryP.objects.all()
	form = PhotoForms
	if request.method == "POST":
		user = request.user.username
		category = request.POST['category']
		image = request.FILES.get('image')
		caption = request.POST['caption']
		
		new_post = P_Post.objects.create(user = user, category = category, image = image, caption = caption)
		new_post.save()
		return redirect('profile')
	return render(request, 'upic.html', {"form" : form, "pics" : pics})

@login_required(login_url='login')
def upvid(request):
	videos = CategoryV.objects.all()
	form = VideoForms
	
	if request.method == "POST":
		user = request.user.username
		category = request.POST['category']
		video = request.FILES.get('video')
		caption = request.POST['caption']

		new_post = V_Post.objects.create(user = user, category = category, video = video, caption = caption)
		new_post.save()
		return redirect('profile')
	return render(request, 'upvid.html', {"form" : form, "videos" : videos})

@login_required(login_url='login')
def cp(request):
	form = CPForms
	if request.method == "POST":
		try:
			category = request.POST['name']
			image = request.FILES.get('thumbnailp')
		
			pform = CategoryP.objects.create(name = category, thumbnailp = image)
			pform.save()
			return redirect('profile')
		except:
			messages.error(request, 'Category Exists')
	return render(request, 'ucp.html', {"form" : form})

@login_required(login_url='login')
def vp(request):
	form = CVForms
	if request.method == "POST":
		try:
			category = request.POST['name']
			image = request.FILES.get('thumbnailv')
		
			vform = CategoryV.objects.create(name = category, thumbnailv = image)
			vform.save()
			return redirect('profile')
		except:
			messages.error(request, 'Category Exists')
	return render(request, 'ucv.html', {"form" : form})


def index(request):
	category = CategoryP.objects.all()
	context = {
		"category" : category
	}
	return render(request, 'index.html', context)

def contact(request):
	return render(request, 'contact.html')

def videos(request):
	fetch_data = CategoryV.objects.all()
	return render(request, 'videos.html', {"fetch_data" : fetch_data})

def about(request):
	return render(request, 'about.html')

def bio(request):
	user = request.GET.get('user')
	user_object = User.objects.get(username = user)
	user_profile = Profile.objects.get(user = user_object)
	user_postp = P_Post.objects.filter(user = user)
	user_postv = V_Post.objects.filter(user = user)
	user_post_length = len(user_postp) + len(user_postv)

	context = {
		"user_object" : user_object,
		"user_profile" : user_profile,
		"user_postp" : user_postp,
		"user_postv" : user_postv,
		"user_post_length" : user_post_length
	}
	return render(request, 'bio.html', context)

def pdetail(request, id):
	category = CategoryP.objects.all()
	de = P_Post.objects.get(id=id)
	img_name = Image.open(de.image)
	width = img_name.width
	height = img_name.height
	forma = img_name.format
	return render(request, 'pdetail.html', {"de" : de, "height" : height, "width" : width, "forma" : forma, "category" : category})

def vdetail(request, id):
	category = CategoryV.objects.all()
	de = V_Post.objects.get(id=id)
	context = {"de" : de, "category" : category}
	return render(request, 'vdetail.html', context)

def categoryp(request):
	category = request.GET.get('category')
	cat = P_Post.objects.filter(category__contains = category)
	return render(request, 'categoryp.html', {"cat" : cat})

def categoryv(request):
	category = request.GET.get('category')
	cat = V_Post.objects.filter(category__contains = category)
	return render(request, 'categoryv.html', {"cat":cat})