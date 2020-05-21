from django.contrib import admin

from profiles_api import models


admin.site.register(models.UserProfile)

# Register your models here so django knows to display the models in admin interface
