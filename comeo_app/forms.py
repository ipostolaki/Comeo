from django import forms

from ckeditor.widgets import CKEditorWidget

from comeo_app.models import Transaction, Campaign
from apps.profiles.models import ComeoUser


class SubscribeForm(forms.Form):
    email = forms.EmailField(max_length=254)


class CampaignForm(forms.ModelForm):
    desc_main = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Campaign
        exclude = ('collected_summ', 'owner', 'tags', 'date_start', 'funding_type',
                   'date_finish', 'date_created', 'views_count', 'state', 'editors')


class FormDonate(forms.ModelForm):
    agree_check = forms.BooleanField(label='Я согласен с правилами')  # TODO: localize

    class Meta:
        model = Transaction
        fields = ['amount', 'method', 'agree_check']

    is_public = forms.BooleanField(label='Опубликовать вклад', initial=True, required=False)  # TODO: localize


class DonateNewUserForm(forms.ModelForm):

    class Meta:
        model = ComeoUser
        fields = ['email', 'first_name']
