from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required

from shared.shortcuts import log_mail


@staff_member_required
def index(request):
    return render(request, 'comeo_debug/index.html')


@staff_member_required
def intended500(request):
    """ This will cause an intended 500 server error. Used to debug logging. """
    a = 500/0


@staff_member_required
def mail_logger_check(request):
    """ This will leave a log record in the log file and will send an email with the same output """
    log_mail.info('comeo_debug view mail_logger_check')
    return render(request, 'comeo_debug/index.html')
