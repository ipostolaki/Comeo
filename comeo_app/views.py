import datetime

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.contrib.auth.decorators import login_required

from comeo_app.logic import transaction_confirmation
from comeo_app.models import Campaign, Transaction, EmailSub
import comeo_app.tasks as tasks
from comeo_app.forms import DonateNewUserForm, FormDonate, SubscribeForm, CampaignForm


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

            return redirect('comeo_app:profile_campaigns')

    else:
        campaign_form = CampaignForm()

    context = {'campaign_form': campaign_form}

    return render(request, 'comeo_app/campaign/campaign_create.html', context)


@login_required
def campaign_edit(request, pk):

    campaign = get_object_or_404(Campaign, pk=pk)

    if request.method == 'GET':
        campaign_form = CampaignForm(instance=campaign)
        published = (campaign.state == campaign.STATE_PUBLIC)
        context = {'campaign_form': campaign_form, 'campaign': campaign, 'published': published}
        return render(request, 'comeo_app/campaign/campaign_edit.html', context)

    elif request.method == 'POST':

        if request.POST.get("delete", False):
            campaign.delete()
        else:
            # Save edited
            campaign_form = CampaignForm(instance=campaign, data=request.POST, files=request.FILES)

            if campaign_form.is_valid():
                # Publish if needed
                if request.POST.get("publish", False):
                    campaign.state = campaign.STATE_PUBLIC
                    start = timezone.now()
                    campaign.date_start = start
                    finish = start + datetime.timedelta(days=campaign.duration)
                    campaign.date_finish = finish
                    tasks.finishCampaign.apply_async((campaign.id,), eta=finish)

                campaign_form.save()

        return redirect('comeo_app:profile_campaigns')


def campaigns_public(request):

    campaigns = Campaign.objects.exclude(state=Campaign.STATE_DRAFT)
    context = {'campaigns': campaigns}
    return render(request, 'comeo_app/campaigns_public.html', context)


def campaign_details(request, pk):

    campaign = get_object_or_404(Campaign, pk=pk)

    if campaign.state == Campaign.STATE_DRAFT:
        # Prevent requesting unpublished campaigns
        return render(request, 'comeo_app/index.html')

    backers_count = Transaction.objects.filter(campaign=campaign, confirmed=True).count()
    context = {'campaign': campaign, 'backers_count': backers_count}
    return render(request, 'comeo_app/campaign_details.html', context)


def campaign_donate(request, pk):

    campaign = get_object_or_404(Campaign, pk=pk)

    if campaign.is_finished():
        # Prevent intentional donate request for finished campaign
        return render(request, 'comeo_app/index.html')

    # TODO: suggest login in case if already registered, but signed out at donation moment

    if not request.user.is_authenticated():
        # Collect unregistered user personal data for donation history
        new_user_form = DonateNewUserForm(request.POST or None)

        if new_user_form.is_valid():
            payer_user = new_user_form.save(commit=False)
            payer_user.set_unusable_password()
        else:
            payer_user = None
    else:
        payer_user = request.user
        new_user_form = None

    donate_form = FormDonate(request.POST or None)
    if payer_user and donate_form.is_valid():
        transaction = donate_form.save(commit=False)
        payer_user.save()
        transaction.payer = payer_user
        transaction.campaign = campaign
        transaction.is_public = donate_form.cleaned_data['is_public']
        transaction.save()

        # Redirect to partner's page with payment instructions, local mock page for now
        return redirect('comeo_app:donate_instruction', transaction_pk=transaction.pk,
                        campaign_pk=campaign.pk)

    context = {'campaign': campaign, 'donate_form': donate_form, 'new_user_form': new_user_form}
    return render(request, 'comeo_app/campaign_donate.html', context)


def donate_instruction(request, transaction_pk, campaign_pk):
    """
    At this step transaction initialization take place.
    Payment partner should process transaction ID for interoperability.
    """
    transaction = get_object_or_404(Transaction, pk=transaction_pk)
    transaction_confirmation(transaction)

    messages.success(request, _('Thanks for your donation! Transaction processing.'))

    return render(request, 'comeo_app/donate_instruction.html',
                  {'pk': transaction_pk, 'campaign_pk': campaign_pk})


def email_subscribe(request):

    subscribe_form = SubscribeForm(request.POST or None)

    if subscribe_form.is_valid():
        email = subscribe_form.cleaned_data['email']
        __, new_created = EmailSub.objects.get_or_create(email=email,
                                                         defaults={'source': 'comeo index page'})

        return render(request, 'comeo_app/email_subscribe_success.html',
                      {'new_created': new_created})

    return render(request, 'comeo_app/index.html', {'subscribe_form': subscribe_form})
