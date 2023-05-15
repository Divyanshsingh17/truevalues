from django.contrib import admin
from accounts.models import User
from image_cropping import ImageCroppingMixin

class UserAdmin(ImageCroppingMixin, admin.ModelAdmin):
    pass

admin.site.register(User, UserAdmin)

# Register your models here.
# admin.site.register(User)