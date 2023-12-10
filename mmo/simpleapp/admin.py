from django.contrib import admin
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from django.utils.translation import gettext_lazy as _
from .models import Player,Category,Post,Response
 
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','player','dateCreation','categoryType')
    list_filter = ('player', 'dateCreation','title','categoryType')
    search_fields = ('title', 'category__name')#

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Player)
admin.site.register(Response)


 