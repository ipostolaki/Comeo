from django import forms
from django.forms import ModelForm

from comeo_app.models import *


# TODO email as username
# TODO credentials match error text

class UserProfileForm(ModelForm):

    class Meta:
        model = Profile
        fields = ['info']

        labels = {'info': 'Info'}


class SignUpForm(ModelForm):

    # Overriding fields of User model - providing details needed for custom form layout

    username = forms.CharField(initial='', label='Username')
    first_name = forms.CharField(initial='', label='First name')
    last_name = forms.CharField(initial='', label='Last name')

    error_messages_email = {'required': 'You definetly need an email.', 'invalid': 'Bad Email!'}
    email = forms.EmailField(initial='', label='Email', error_messages=error_messages_email)

    error_messages_password = {'required': 'You definetly need a password.', 'max_length': 'max_length',
                      'min_length is 5': 'min_length'}
    password = forms.CharField(initial='', label='Password', max_length=100, min_length=5, error_messages=error_messages_password)

    class Meta:
        model = User # form based on standard Django user model
        # only necessary fields prepared for rendering
        fields = ['username', 'first_name', 'last_name', 'email', 'password']


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


# class LoginForm(forms.Form):
#     username = forms.CharField(initial='', label='Username:', error_messages={'required': 'Username?'})
#     password = forms.CharField(initial='', widget=forms.PasswordInput(render_value=True), label='Password:',
#                                max_length=100, min_length=5, error_messages={'required': 'Password?'})



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