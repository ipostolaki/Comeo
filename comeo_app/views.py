from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from comeo_app.forms import *
from django.core.mail import send_mail


from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'comeo_app/index.html')


def faq(request):
    return render(request, 'comeo_app/faq.html')

def about(request):
    return render(request, 'comeo_app/about.html')


def signup(request):

    registered = False

    if request.method == 'POST':
        sign_up_form = SignUpForm(request.POST)

        if sign_up_form.is_valid():

            user = sign_up_form.save()
            user.set_password(user.password)
            user.save()
            registered = True

            authenticated_user = authenticate(email=sign_up_form.cleaned_data['email'], password=sign_up_form.cleaned_data['password'])

            if authenticated_user:
                login(request, authenticated_user)
    else:
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

# TODO next hidden input in forms


@login_required
def profile(request):
    return render(request, 'comeo_app/profile.html')


@login_required
def profile_edit(request):

    profile = request.user.profile

    if request.method == 'POST':

        user_form = EditProfileForm(instance=request.user, data=request.POST)
        profile_form = ProfileForm(instance=profile, data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            saved_profile = profile_form.save()
            print(saved_profile.bank_account)
            saved_user = user_form.save(commit=False)
            saved_user.profile = saved_profile
            saved_user.save()


            # TODO: 'profile saved' notification message in template
            # TODO: confirm email change through token link

    else:
        profile_form = ProfileForm(instance=profile)
        user_form = EditProfileForm(instance=request.user)

    # user = User.objects.get(profile=request.user.profile)

    context = {'profile_form': profile_form, 'user_form': user_form}

    return render(request, 'comeo_app/profile_edit.html', context)
