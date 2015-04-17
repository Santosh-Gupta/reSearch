from django.contrib import admin

# Register your models here.
from .models import Join

class JoinAdmin(admin.ModelAdmin):
    list_display = ['__unicode__', 'search_string', 'timestamp', 'updated']
    class Meta:
        model= Join


admin.site.register(Join, JoinAdmin)