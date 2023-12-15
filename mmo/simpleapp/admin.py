from django.contrib import admin
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from django.utils.translation import gettext_lazy as _
from .models import Post,Response
 


admin.site.register(Post)
admin.site.register(Response)


 