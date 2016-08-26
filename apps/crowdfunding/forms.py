from django import forms
from django.utils.translation import ugettext_lazy as _
from ckeditor.widgets import CKEditorWidget

from apps.crowdfunding.models import Transaction, Campaign
from apps.profiles.models import ComeoUser


class CampaignForm(forms.ModelForm):
    desc_main = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Campaign
        exclude = ('collected_sum', 'owner', 'tags', 'date_start', 'funding_type',
                   'date_finish', 'date_created', 'views_count', 'state', 'editors')


class FormDonate(forms.ModelForm):
    agree_check = forms.BooleanField(label=_('I agree to the rules'))
    is_public = forms.BooleanField(label=_('Public donation'), initial=True, required=False)

    class Meta:
        model = Transaction
        fields = ['amount', 'method', 'agree_check']


class DonateNewUserForm(forms.ModelForm):
    class Meta:
        model = ComeoUser
        fields = ['email', 'first_name']
