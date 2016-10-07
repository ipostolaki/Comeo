import logging


"""
log

This shortcut may be used for logging inside of django apps modules, instead of logging.getLogger()
Thus to log a message it is necessary just to import 'log' from this module.
Explicit 'apps' logger name is used here.
This logger have a LOGGING configuration in django settings file common.py
"""
log = logging.getLogger('apps')

"""
log_mail

This shortcut may be used to inform admin about some actions unrelated to errors
"""
log_mail = logging.getLogger('mail.intended')
