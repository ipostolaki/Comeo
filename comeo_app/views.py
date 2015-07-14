from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from comeo_app.forms import *
from django.utils.translation import ugettext
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _

from comeo_app.models import *

# check
import datetime
from django.utils import dateformat
from django.utils import timezone
# check

#import smtplib
#from email.mime.text import MIMEText



from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'comeo_app/index.html')


def test(request):

    campaigns = Campaign.objects.all()

    context = {'campaigns': campaigns}

    return render(request, 'comeo_app/test.html', context)


def faq(request):
    return render(request, 'comeo_app/faq.html')


def about(request):
    return render(request, 'comeo_app/about.html')


# experimental
def send_email(request):
    print('sent')
    # send_mail('Subject here', 'Here is the message.', 'contact@comeo.org.md',['ilia.ravemd@gmail.com'], fail_silently=False)
    return HttpResponseRedirect('http://comeo.cf')


def email_subscribe(request):

    if request.method == 'POST':
        subscribe_form = SubscribeForm(request.POST)

        if request.POST['email']:

            email = request.POST['email']

            print(email)
            sub = EmailSub(email=request.POST['email'], source="comeo")
            sub.save(force_insert=True)

            return HttpResponseRedirect('/email-subscribe/success')

    return render(request, 'comeo_app/index.html')



def email_subscribe_success(request):
    return render(request, 'comeo_app/email_subscribe_success.html')


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

# TODO next hidden input in forms for redirect


@login_required
def profile(request):
    return render(request, 'comeo_app/profile/profile.html')


@login_required
def profile_edit(request):

    profile = request.user.profile

    if request.method == 'POST':

        # print(request.FILES['photo'])

        user_form = EditUserForm(instance=request.user, data=request.POST)

        # TODO Model Factory instead
        profile_form = ProfileForm(instance=profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():

            saved_profile = profile_form.save()
            saved_user = user_form.save(commit=False)
            saved_user.profile = saved_profile
            saved_user.save()

            messages.success(request, _('profile updated'))

            # TODO: 'profile saved' notification message in template
            # TODO: confirm email change through token link

    else:
        profile_form = ProfileForm(instance=profile)
        user_form = EditUserForm(instance=request.user)

    # user = User.objects.get(profile=request.user.profile)

    context = {'profile_form': profile_form, 'user_form': user_form}

    return render(request, 'comeo_app/profile/profile_edit.html', context)


def ro(request):
    return render(request, 'comeo_app/ro.html', {'lang': 'ro'})


def campaign_create(request):

    if request.method == 'POST':
        campaign_form = CampaignForm(data=request.POST, files=request.FILES)

        if campaign_form.is_valid():

            created_campaign = campaign_form.save(commit=False)
            created_campaign.start_date = '2015-07-03' # YYYY-MM-DD HH:MM
            created_campaign.save()

            created_campaign.owner.add(request.user)
            created_campaign.save()
            return HttpResponseRedirect(reverse('comeo_app:profile_campaigns'))

    else:
        campaign_form = CampaignForm()

    context = {'campaign_form': campaign_form}

    return render(request, 'comeo_app/campaign/campaign_create.html', context)


def profile_campaigns(request):

    # campaigns = request.user.campaign_set.all()
    campaigns = Campaign.objects.filter(owner=request.user)

    context = {'campaigns': campaigns}
    return render(request, 'comeo_app/profile/profile_campaigns.html', context)


def campaign_edit(request, pk):

    campaign = Campaign.objects.get(pk=pk)

    if request.method == 'GET':
        campaign_form = CampaignForm(instance=campaign)
        context = {'campaign_form': campaign_form, 'campaign': campaign}
        return render(request, 'comeo_app/campaign/campaign_edit.html', context)

    elif request.method == 'POST':

        if request.POST.get("delete", False):
            campaign.delete()
        else:
            # save
            campaign_form = CampaignForm(instance=campaign, data=request.POST, files=request.FILES)
            if campaign_form.is_valid(): campaign_form.save()

        return HttpResponseRedirect(reverse('comeo_app:profile_campaigns'))


def campaigns_public(request):

    campaigns = Campaign.objects.all()

    context = {'campaigns': campaigns}

    return render(request, 'comeo_app/campaigns_public.html', context)