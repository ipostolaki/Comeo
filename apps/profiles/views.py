from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.translation import ugettext_lazy as _

from apps.crowdfunding.models import Campaign
from apps.registry import graph_interface
from .forms import EditUserForm, ProfileForm, SignUpForm
from .models import ComeoUser
from shared.shortcuts import log


def signup(request):

    if request.method == 'POST':
        sign_up_form = SignUpForm(request.POST)

        if sign_up_form.is_valid():
            user = sign_up_form.save(commit=False)
            user.set_password(user.password)
            user.save()

            # According to Django guidelines: "you must successfully authenticate the
            # user with authenticate() before you call login()"
            authenticated_user = authenticate(email=sign_up_form.cleaned_data['email'],
                                              password=sign_up_form.cleaned_data['password'])
            if authenticated_user:
                login(request, authenticated_user)

            # create a new Person node in the graph database
            graph_interface.Person.create_person(authenticated_user.id)

            log.info("New user registered: %s", authenticated_user.get_full_name())

            messages.success(request, _('Welcome ') + user.get_short_name() + '!')
            return redirect('profiles:profile')
    else:
        sign_up_form = SignUpForm(initial={'first_name': '', 'email': '',
                                           'last_name': '', 'password': ''})

    context = {'sign_up_form': sign_up_form}
    return render(request, 'profiles/auth/signup.html', context)


@login_required
def profile(request):
    """
    View for user's own profile
    """
    context = {
        'resources': graph_interface.Person.get_resources(request.user.id),
        'skills': graph_interface.Person.get_skills(request.user.id),
        'interests': graph_interface.Person.get_interests(request.user.id),
        'subject_user': request.user
    }
    return render(request, 'profiles/profile.html', context)


def public_profile(request, django_user_id):
    user = get_object_or_404(ComeoUser, id=django_user_id)
    return render(request, 'profiles/public_profile.html', {'subject_user': user})


@login_required
def profile_settings(request):
    profile = request.user.profile

    if request.method == 'POST':
        user_form = EditUserForm(instance=request.user, data=request.POST)
        profile_form = ProfileForm(instance=profile, data=request.POST, files=request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            saved_profile = profile_form.save()
            saved_user = user_form.save(commit=False)
            saved_user.profile = saved_profile
            saved_user.save()

            messages.success(request, _('Your changes were saved'))
            return redirect('profiles:profile')
    else:
        profile_form = ProfileForm(instance=profile)
        user_form = EditUserForm(instance=request.user)

    context = {'profile_form': profile_form, 'user_form': user_form}
    return render(request, 'profiles/profile_settings.html', context)


@login_required
def profile_campaigns(request):
    campaigns = Campaign.objects.filter(editors=request.user)
    context = {'campaigns': campaigns}
    return render(request, 'profiles/profile_campaigns.html', context)
