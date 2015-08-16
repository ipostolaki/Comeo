from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from comeo_app.forms import *
from django.utils.translation import ugettext
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _
from django.db.models import Q
from django.utils import timezone
from comeo_app.logic import *

from comeo_app.models import *

import datetime

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

            return HttpResponseRedirect('/email-subscribe/success') # TODO: redirect shortcut instead

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

        user_form = EditUserForm(instance=request.user, data=request.POST)

        # TODO Model Factory instead
        profile_form = ProfileForm(instance=profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():

            saved_profile = profile_form.save()
            saved_user = user_form.save(commit=False)
            saved_user.profile = saved_profile
            saved_user.save()

            messages.success(request, _('profile updated'))

            # TODO: confirm email change through token link

    else:
        profile_form = ProfileForm(instance=profile)
        user_form = EditUserForm(instance=request.user)

    context = {'profile_form': profile_form, 'user_form': user_form}

    return render(request, 'comeo_app/profile/profile_edit.html', context)


def ro(request):
    return render(request, 'comeo_app/ro.html', {'lang': 'ro'})

@login_required
def campaign_create(request):

    if request.method == 'POST':
        campaign_form = CampaignForm(data=request.POST, files=request.FILES)

        if campaign_form.is_valid():

            created_campaign = campaign_form.save(commit=False)
            created_campaign.save()

            created_campaign.owner = request.user
            created_campaign.editors.add(request.user)
            created_campaign.save()

            return HttpResponseRedirect(reverse('comeo_app:profile_campaigns'))

    else:
        campaign_form = CampaignForm()

    context = {'campaign_form': campaign_form}

    return render(request, 'comeo_app/campaign/campaign_create.html', context)


@login_required
def profile_campaigns(request):

    campaigns = Campaign.objects.filter(editors=request.user)
    # TODO: now all owners are editors by default(should not be?) May need refactoring - distinct should work properly on PSQL not sqlite
    # campaigns = Campaign.objects.filter(Q(owner=request.user) | Q(editors=request.user)).distinct()

    context = {'campaigns': campaigns}
    return render(request, 'comeo_app/profile/profile_campaigns.html', context)


@login_required
def campaign_edit(request, pk):

    campaign = Campaign.objects.get(pk=pk)

    campaign.days_to_finish()

    if request.method == 'GET':
        campaign_form = CampaignForm(instance=campaign)
        published = (campaign.state==campaign.STATE_PUBLIC)
        context = {'campaign_form': campaign_form, 'campaign': campaign, 'published': published}
        return render(request, 'comeo_app/campaign/campaign_edit.html', context)

    elif request.method == 'POST':

        if request.POST.get("delete", False):
            campaign.delete()
        else:
            # save edited
            campaign_form = CampaignForm(instance=campaign, data=request.POST, files=request.FILES)

            if campaign_form.is_valid():

                # publish if needed
                if request.POST.get("publish", False):
                    campaign.state = campaign.STATE_PUBLIC
                    start = timezone.now()
                    campaign.date_start = start
                    finish = start + datetime.timedelta(days=campaign.duration)
                    campaign.date_finish = finish

                campaign_form.save()

        return HttpResponseRedirect(reverse('comeo_app:profile_campaigns'))


def campaigns_public(request):

    campaigns = Campaign.objects.filter(state=Campaign.STATE_PUBLIC)

    context = {'campaigns': campaigns}

    return render(request, 'comeo_app/campaigns_public.html', context)


def campaign_details(request, pk):

    # TODO: restrict viewing unpublished campaigns

    campaign = Campaign.objects.get(pk=pk)

    backers_count = Transaction.objects.filter(campaign=campaign, confirmed=True).count()

    context = {'campaign': campaign, 'backers_count': backers_count}

    return render(request, 'comeo_app/campaign_details.html', context)


def campaign_donate(request, pk):

    campaign = Campaign.objects.get(pk=pk)

    donate_form = FormDonate(request.POST or None)

    if donate_form.is_valid():
        transaction = donate_form.save(commit=False)
        transaction.payer = request.user
        transaction.campaign = campaign
        transaction.save()
        # TODO refactor? crete trans in next view, send just amount/method (session)


        #messages.success(request, _('Thanks for your donation!'))
        # TODO refactor shortcut
        #return HttpResponseRedirect(reverse('comeo_app:campaign_details', kwargs={'pk': pk}))

        # redirect to partners page with payment instructions
        return HttpResponseRedirect(reverse('comeo_app:donate_instruction', kwargs={'transaction_pk': transaction.pk, 'campaign_pk': campaign.pk}))


    context = {'campaign': campaign, 'donate_form': donate_form}

    return render(request, 'comeo_app/campaign_donate.html', context)


def donate_instruction(request, transaction_pk, campaign_pk):

    # TODO security: this view can be called by anyone through get request with any combination of transaction id and campaign id

    '''
    At this step transaction initialization take place.
    Payment partner should process transaction ID for interoperability
    '''


    t = Transaction.objects.get(pk=transaction_pk)
    transaction_confirmation(t)

    messages.success(request, _('Thanks for your donation! Transaction processing.'))

    return render(request, 'comeo_app/donate_instruction.html', {'pk': transaction_pk, 'campaign_pk': campaign_pk})
