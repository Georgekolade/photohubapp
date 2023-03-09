from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	path('', views.index, name = 'index'),
	path('about/', views.about, name = 'about'),
	path('bio/', views.bio, name = 'bio'),
	path('profile/upic', views.upic, name = 'upic'),
	path('profile/upvid', views.upvid, name = 'upvid'),
	path('profile/', views.profile, name = 'profile'),
	path('videos/', views.videos, name = 'videos'),
	path('pdetail/<str:id>', views.pdetail, name = 'pdetail'),
	path('vdetail/<str:id>', views.vdetail, name = 'vdetail'),
	path('profile/cp', views.cp, name = 'cp'),
	path('profile/vp', views.vp, name = 'vp'),
	path('categoryp/', views.categoryp, name = 'categoryp'),
	path('categoryv/', views.categoryv, name = 'categoryv'),
	path('contact/', views.contact, name = 'contact'),
	path('register/', views.register, name = 'register'),
	path('login/', views.login, name = 'login'),
	path('logout/', views.logout, name = 'logout')
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
