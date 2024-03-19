from django.contrib import admin
from .models import Molde, MoldeItem

class MoldeItemInline(admin.TabularInline):
    model = MoldeItem
    extra = 1

class MoldeAdmin(admin.ModelAdmin):
    inlines = [MoldeItemInline]

admin.site.register(Molde, MoldeAdmin)
