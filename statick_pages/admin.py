from django.contrib import admin
from django.contrib.flatpages.models import FlatPage

# Note: we are renaming the original Admin and Form as we import them!
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.admin import FlatpageForm

from django import forms
from ckeditor.widgets import CKEditorWidget

class StatickPageForm(FlatpageForm):
    content = forms.CharField(widget=CKEditorWidget(config_name='default_config'))

    class Meta:
        model = FlatPage # this is not automatically inherited from FlatpageFormOld


class StatickPageAdmin(FlatPageAdmin):
    form = StatickPageForm


# We have to unregister the normal admin, and then reregister ours
admin.site.unregister(FlatPage)
admin.site.register(FlatPage, StatickPageAdmin)

