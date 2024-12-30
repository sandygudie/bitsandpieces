from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Blog, Tag

class SummerAdmin(SummernoteModelAdmin):  
      summernote_fields = ('content')
    
    
admin.site.register(Blog, SummerAdmin)
admin.site.register(Tag)
