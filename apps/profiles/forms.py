from django import forms
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm

from .models import Profile, ComeoUser


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


class AdminUserCreationForm(UserCreationForm):

    def __init__(self, *args, **kargs):
        super(AdminUserCreationForm, self).__init__(*args, **kargs)

    class Meta:
        model = ComeoUser
        fields = '__all__'


class AdminUserChangeForm(UserChangeForm):

    def __init__(self, *args, **kargs):
        super(AdminUserChangeForm, self).__init__(*args, **kargs)

    class Meta:
        model = ComeoUser
        fields = '__all__'
