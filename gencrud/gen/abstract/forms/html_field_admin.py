from ckeditor.widgets import CKEditorWidget
from django import forms


class HTMLFieldAdminForm(forms.ModelForm):
    html = forms.CharField(widget=CKEditorWidget())
