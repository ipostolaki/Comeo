from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django.utils.translation import ugettext_lazy as _

from ckeditor.widgets import CKEditorWidget

from comeo_app.models import Transaction, Profile, Campaign, ComeoUser


class SubscribeForm(forms.Form):
    email = forms.EmailField(max_length=254)


class LoginForm(AuthenticationForm):
    username = forms.EmailField(max_length=254)
    password = forms.CharField(label=_("Password"), widget=forms.PasswordInput)


class SignUpForm(forms.ModelForm):
    password = forms.CharField(min_length=5, label=_('Password'))

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'email', 'password']


class EditUserForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'email']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class CampaignForm(forms.ModelForm):
    desc_main = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Campaign
        exclude = ('collected_summ', 'owner', 'tags', 'date_start', 'funding_type',
                   'date_finish', 'date_created', 'views_count', 'state', 'editors')


# ----------------- Admin user management Forms

class CustomUserCreationForm(UserCreationForm):

    def __init__(self, *args, **kargs):
        super(CustomUserCreationForm, self).__init__(*args, **kargs)

    class Meta:
        model = ComeoUser
        fields = '__all__'


class CustomUserChangeForm(UserChangeForm):

    def __init__(self, *args, **kargs):
        super(CustomUserChangeForm, self).__init__(*args, **kargs)

    class Meta:
        model = ComeoUser
        fields = '__all__'

# / ----------------- Admin user management Forms


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
