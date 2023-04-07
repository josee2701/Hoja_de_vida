from django.contrib import admin

from .models import Profile, Education,Experience,Contact,Skill,Interest,Professional_profile

# Register your models here.

admin.site.register(Profile)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Contact)
admin.site.register(Skill)
admin.site.register(Interest)
admin.site.register(Professional_profile)
