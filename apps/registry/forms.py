from django import forms


class EditGraphItemForm(forms.Form):
    title = forms.CharField()
    metadata = forms.CharField(widget=forms.Textarea,
                               required=False,
                               label="Description (optional)"  #TODO: localize
                               )