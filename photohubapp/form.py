from django import forms
from .models import P_Post, V_Post, CategoryP, CategoryV

class PhotoForms(forms.ModelForm):
	class Meta:
		model = P_Post
		fields = ['image', 'caption']
		widgets = {
			'image' : forms.FileInput(attrs={'class' : 'form-control', 'name' : 'image'}),
			'caption' : forms.Textarea(attrs={'class' : 'form-control', 'rows' : '2', 'name' : 'caption'})
		}

class VideoForms(forms.ModelForm):
	class Meta:
		model = V_Post
		fields = ['video', 'caption']
		widgets = {
			'video' : forms.FileInput(attrs={'class' : 'form-control', 'name' : 'video'}),
			'caption' : forms.Textarea(attrs={'class' : 'form-control', 'rows' : '2', 'name' : 'caption'})
		}

class CPForms(forms.ModelForm):
	class Meta:
		model = CategoryP
		fields = ['name', 'thumbnailp']
		widgets = {
			'name' : forms.TextInput(attrs={'class' : 'form-control', 'name' : 'name'}),
			'thumbnailp' : forms.FileInput(attrs={'class' : 'form-control', 'name' : 'thumbnailp'})
		}

class CVForms(forms.ModelForm):
	class Meta:
		model = CategoryV
		fields = ['name', 'thumbnailv']
		widgets = {
			'name' : forms.TextInput(attrs={'class' : 'form-control', 'name' : 'name'}),
			'thumbnailv' : forms.FileInput(attrs={'class' : 'form-control', 'name' : 'thumbnailv'})
		}