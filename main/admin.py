from django.contrib import admin

from .models import Land

@admin.register(Land)
class LandAdmin(admin.ModelAdmin):
    search_fields = ['farmer_name', 'crops']
    list_filter = ['season']
