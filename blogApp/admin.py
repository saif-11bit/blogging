from django.contrib import admin
from django.forms import TextInput
from django.db import models
from .models import Blog, Contact, Subscriber, Crousal, UserProfile
from tinymce.widgets import TinyMCE

# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    formfield_overrides = {
    	models.TextField: {"widget": TinyMCE()},
        models.CharField: {'widget': TextInput(attrs={'size':'100'})},
    }


admin.site.register(Blog, BlogAdmin)
admin.site.register(Contact)
admin.site.register(Subscriber)
admin.site.register(Crousal)
admin.site.register(UserProfile)