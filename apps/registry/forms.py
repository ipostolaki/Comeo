from django import forms
from django.utils.translation import ugettext_lazy as _


class EditGraphItemForm(forms.Form):
    title = forms.CharField()
    metadata = forms.CharField(widget=forms.Textarea,
                               required=False,
                               label=_("Description (optional)")
                               )
