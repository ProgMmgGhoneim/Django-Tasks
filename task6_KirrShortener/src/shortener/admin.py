from django.contrib import admin

from .models import KirURLModel

# Register your models here.

class URLModelAdmin(admin.ModelAdmin):
    list_display = ('Url','Shortcode','TimeCreate','Update')
    list_filter  = ('TimeCreate' , 'Url' )
    list_per_page = 5

admin.site.register(KirURLModel ,URLModelAdmin)
