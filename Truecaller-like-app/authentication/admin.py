from django.contrib import admin

from authentication.models import Contact, CustomUser, Spam

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Contact)
admin.site.register(Spam)
