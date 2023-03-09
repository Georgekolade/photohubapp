from django.contrib import admin
from .models import Profile, P_Post, V_Post, CategoryP, CategoryV

# Register your models here.
admin.site.register(Profile)
admin.site.register(P_Post)
admin.site.register(V_Post)
admin.site.register(CategoryP)
admin.site.register(CategoryV)