from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from comeo_app.forms import *
from django.core.mail import send_mail


from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'comeo_app/index.html')


def signup(request):

    registered = False

    if request.method == 'POST':
        sign_up_form = SignUpForm(request.POST)

        # TODO check for double email, the Django way
        if sign_up_form.is_valid():

            user = sign_up_form.save()
            user.set_password(user.password)
            user.save()

            registered = True

            # TODO is authenticate needed?

            signed_up_user = authenticate(email=sign_up_form.cleaned_data['email'], password=sign_up_form.cleaned_data['password'])

            if signed_up_user is not None:
                login(request, signed_up_user)
    else:
        # sign_up_form = SignUpForm(initial={'first_name': '', 'email': '', 'last_name': '', 'password': ''})
        sign_up_form = SignUpForm(initial={'first_name': '', 'email': '', 'last_name': '', 'password': ''})

    context = {'sign_up_form': sign_up_form, 'registered': registered}

    return render(request, 'comeo_app/signup.html', context)


# TODO send registration confirmation email (active user check ?)
# TODO non form fields errors logging / output
# TODO double POST ?
# TODO password reset
# TODO Password confirmation
# TODO built-in Django Registration forms/urls

# TODO custom User model with email instead of username ?

# def login_view(request):
#
#     if request.method == 'POST':
#         login_form = LoginForm(request.POST)
#
#         if login_form.is_valid():
#             username = request.POST['username']
#             password = request.POST['password']
#
#             user = authenticate(username=username, password=password)
#
#             if user is not None:
#                 if user.is_active:
#                     login(request, user)
#
#                     return HttpResponseRedirect('/profile/')
#
#                 else:
#                     return HttpResponse('Activation needed')
#             else:
#                 # TODO check what is wrong - pass / username
#                 login_form.add_error(field=None, error="Hey, password and username does not match. Are you registered?")
#     else:
#         login_form = LoginForm()
#
#     return render(request, 'comeo_app/login.html', {'login_form': login_form})
# # TODO next hidden input in forms


def user_logout(request):

    logout(request)
    return HttpResponseRedirect('/')

@login_required
def profile(request):
    return render(request, 'comeo_app/profile.html')


@login_required
def profile_edit(request):

    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST)
        user_form = SignUpForm(request.POST)

        # profile_form.save()

        if profile_form.is_valid() and user_form.is_valid():
            print('OK')
    else:
        profile_form = UserProfileForm()
        user_form = SignUpForm(instance=request.user)

    # user = User.objects.get(profile=request.user.profile)

    context = {'profile_form': profile_form, 'user_form': user_form}

    return render(request, 'comeo_app/profile_edit.html', context)
