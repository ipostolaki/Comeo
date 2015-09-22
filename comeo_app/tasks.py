from celery import shared_task
from comeo_app.models import Campaign

@shared_task
def finishCampaign(campaign_id):

    campaign = Campaign.objects.get(id=campaign_id)

    if campaign.collected_summ >= campaign.summ_goal:
        campaign.state = Campaign.STATE_FINISHED_SUCCESSFULLY
    else:
        campaign.state = Campaign.STATE_FINISHED_NON_SUCCESSFULLY

    campaign.save()