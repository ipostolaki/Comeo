from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail

from apps.events.forms import EventPaymentForm
from shared.shortcuts import log

from apps.events.pyCoinPayments.pyCoinPayments import CryptoPayments


API_KEY     = 'cc111306d9ddaa67de94652a99d9a6b56b850535e18887efe957cc4dc1b85ffb'
API_SECRET  = b'aefb1CeC3aa9b7CB104da05Ed9048CE138f021075CdB8B27D15fD504869b18B0'
IPN_URL = 'https://my.webhookrelay.com/v1/webhooks/1185df80-c62d-41cb-944f-acb37ea04beb'


def events_public(request):
    return render(request, 'events/events_public.html')


def event_details(request):

    event_payment_form = EventPaymentForm(request.POST or None)

    if request.method == 'POST':
        # process payment intention

        if event_payment_form.is_valid():

            # collect data and create transaction

            selected_currency = request.POST.get("currencyOptions")
            first_name = event_payment_form.cleaned_data['first_name']
            last_name = event_payment_form.cleaned_data['last_name']
            email = event_payment_form.cleaned_data['email']

            payment_url = process_payment(
                selected_currency, first_name, last_name, email)

            # redirect customer to the crypto PSP payment page
            return redirect(payment_url)

    context = {'event_payment_form':event_payment_form}
    return render(request, 'events/event_details.html', context)



def process_payment(currency, first_name, last_name, email):

    log.info("Creating %s transaction for: %s %s %s", currency, first_name, last_name, email)

    client = CryptoPayments(API_KEY, API_SECRET, IPN_URL)

    # Create Transaction

    post_params = {
        'amount' : '10',
        'currency1' : 'EUR',
        'currency2' : currency,
        'success_url': 'http://comeo.co',
        'buyer_email': email,
        'buyer_name': first_name,
    }

    transaction = client.createTransaction(post_params)
    log.info(transaction)

    return transaction.status_url

@csrf_exempt
def coinpayments_ipn(request):
    log.info('Received webhook data from coinpayments')
    log.info(request)
    # request.POST['txn_id']

    email = request.POST.get('email')
    status = request.POST.get('status')

    if status=='1':
        if email:
            log.info('Sending email to %s', email)
            send_mail("Your ticket", "You have paid for a ticket with cryptocurrency! \n \n TICKET DATA PLACEHOLDER", 'info@comeo.co', [email])
    else:
        log.info('Transaction status is not 1, status is %s', status)

    return HttpResponse('200 ok')

