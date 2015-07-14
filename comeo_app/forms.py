from django import forms

from comeo_app.models import *

from django.contrib.auth import get_user_model

from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm

from django.utils.translation import ugettext_lazy as _

# TODO email as username
# TODO credentials match error text

# class UserProfileForm(ModelForm):
#
#     class Meta:
#         model = Profile
#         fields = ['info']
#         # labels = {'info': 'Info'}


class SubscribeForm(forms.Form):
    email = forms.EmailField(max_length=254)

# TODO: need to be subclassed to localize ??
class LoginForm(AuthenticationForm):
    username = forms.EmailField(max_length=254)
    password = forms.CharField(label=_("Password"), widget=forms.PasswordInput)

    # error_messages = {
    #     'invalid_login': _("Please enter a correct %(username)s and password. "
    #                        "Note that both fields may be case-sensitive."),
    #     'inactive': _("This account is inactive."),
    # }


class SignUpForm(forms.ModelForm):

    last_name = forms.CharField(required=True, label=_('last name'))
    password = forms.CharField(min_length=5, label=_('Password'))
    # TODO pass length check at: reset, change, login?

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'email', 'password']

    # def __init__(self, *args, **kwargs):
    # super(MyModelForm, self).__init__(*args, **kwargs)
    # # Making name required
    # self.fields['name'].required = True
    # self.fields['age'].required = True
    # self.fields['bio'].required = True
    # self.fields['profession'].required = True


class EditUserForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'email']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

# class EditProfileForm(forms.Form):
#
#     email = forms.EmailField()
#     first_name = forms.CharField()
#     last_name = forms.CharField()
#     info = forms.CharField(widget=forms.Textarea)


class CampaignForm(forms.ModelForm):
    class Meta:
        model = Campaign
        exclude = ('collected_summ','owner', 'tags', 'funding_type', 'start_date')

# ----------------- Admin user management Forms

class CustomUserCreationForm(UserCreationForm):

    def __init__(self, *args, **kargs):
        super(CustomUserCreationForm, self).__init__(*args, **kargs)
        del self.fields['username']

    class Meta:
        model = ComeoUser
        fields = '__all__'


class CustomUserChangeForm(UserChangeForm):

    def __init__(self, *args, **kargs):
        super(CustomUserChangeForm, self).__init__(*args, **kargs)
        del self.fields['username']

    class Meta:
        model = ComeoUser
        fields = '__all__'

# END ----------------- Admin user management Forms







# class ProfileEditForm(SignUpForm):
#     class Meta:
#         model = User
#         fields = ['username', 'first_name', 'last_name', 'email', 'password']



from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Div
from crispy_forms.bootstrap import StrictButton


# class CrispyForm(forms.Form):
#     username = forms.CharField(label='Username')
#     password = forms.CharField(widget=forms.PasswordInput(render_value=True), label='password', max_length=100,
#                                min_length=10, error_messages={'required': 'You definetly need a password.'})
#
#     def __init__(self, *args, **kwargs):
#         super(CrispyForm, self).__init__(*args, **kwargs)
#         self.helper = FormHelper()
#         self.helper.form_method = 'post'
#         self.helper.form_action = '/login/'
#         self.helper.form_tag = True
#         self.helper.form_class = 'form-horizontal'
#         self.helper.label_class = 'col-lg-5'
#         self.helper.field_class = 'col-lg-3'
#         self.helper.layout = Layout(
#             'username',
#             'password',
#             Div(Div(Submit('login', 'Login'), css_class="col-lg-offset-5 col-lg-7"), css_class="form-group")
#         )





# class UserForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput())
#
#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password')
#
#
# class UserProfileForm(forms.ModelForm):
#     class Meta:
#         model = UserProfile
#         fields = ('text', 'photo')



# class FormSignUpForm(forms.Form):
#
#
#     first_name = forms.CharField(initial='', label='First name')
#     last_name = forms.CharField(initial='', label='Last name')
#     error_messages_email = {'required': 'You definetly need an email.', 'invalid': 'Bad Email!'}
#     email = forms.EmailField(initial='', label='Email', error_messages=error_messages_email)
#
#     error_messages_password = {'required': 'You definetly need a password.', 'max_length': 'max_length',
#                       'min_length is 5': 'min_length'}
#
#     password = forms.CharField(initial='', label='Password',
#                                max_length=100, min_length=5, error_messages=error_messages_password)