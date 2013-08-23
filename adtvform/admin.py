from django.contrib import admin
from adtvform.models import Search

class SearchAdmin(admin.ModelAdmin):
    list_display = ('sdata', 'sdate')
    search_fields = ['sdata']


    
admin.site.register(Search, SearchAdmin)