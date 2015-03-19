from django.contrib import admin
from settings.models import Section, SettingsGroup, Field


class SectionAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'system_name': ('title',),
    }

admin.site.register(Section, SectionAdmin)
admin.site.register(SettingsGroup)
admin.site.register(Field)
