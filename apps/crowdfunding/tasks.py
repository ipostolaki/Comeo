from celery import shared_task

from apps.crowdfunding.models import Campaign


@shared_task
def finish_campaign(campaign_id):
    campaign = Campaign.objects.get(id=campaign_id)

    if campaign.collected_sum >= campaign.sum_goal:
        campaign.state = Campaign.STATE_FINISHED_SUCCESSFULLY
    else:
        campaign.state = Campaign.STATE_FINISHED_NON_SUCCESSFULLY

    campaign.save()
