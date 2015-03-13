from django.contrib import admin
from settings.models import Section, SettingsGroup, FieldGroup, Field

class SectionAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'system_name': ('title',),
    }

admin.site.register(Section, SectionAdmin)
admin.site.register(FieldGroup)
admin.site.register(Field)
admin.site.register(SettingsGroup)
