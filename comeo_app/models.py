from django.conf import settings
from django.db import models
from django.utils import timezone
from django.core.mail import send_mail
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

from django.utils.translation import ugettext_lazy as _


class Profile(models.Model):

    bank_account = models.CharField(verbose_name=_('bank account'), max_length=300, blank=True)
    buletin_number = models.CharField(verbose_name=_('buletin number'), max_length=50, blank=True)
    photo = models.FileField(verbose_name=_('photo'), blank=True, upload_to='users_photos')


class CustomUserManager(BaseUserManager):

    def _create_user(self, email, password,
                     is_staff, is_superuser, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        now = timezone.now()
        if not email:
            raise ValueError('Email must be set')

        email = self.normalize_email(email)
        user = self.model(email=email,
                          is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser, last_login=now,
                          date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        return self._create_user(email, password, False, False,
                                 **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(email, password, True, True,
                                 **extra_fields)


class ComeoUser(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(_('Email'), max_length=254, unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=False)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    is_staff = models.BooleanField(_('staff status'), default=False)
    is_active = models.BooleanField(_('active'), default=True)
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    profile = models.OneToOneField(Profile, null=True, verbose_name=_('user profile'))

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')


    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        "Returns the short name for the user."
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, from_email, [self.email], **kwargs)


class EmailSub(models.Model):

    source = models.CharField(verbose_name=_('source'), max_length=300, blank=True)
    email = models.EmailField(_('Email'), max_length=254)


class Tag(models.Model):
    name = models.CharField(max_length=100)


class Campaign(models.Model):

    #### state choices

    STATE_DRAFT = 'draft'
    STATE_PUBLIC = 'public'
    STATE_COMPLETE = 'complete'

    STATES = (
        (STATE_DRAFT, 'draft'),
        (STATE_PUBLIC, 'public'),
        (STATE_COMPLETE, 'complete'),
    )

    #### funding choices

    FUND_CONDITIONAL = 'conditional'
    FUND_UNCONDITIONAL = 'unconditional'

    FUND_TYPES = (
        (FUND_CONDITIONAL, 'conditional'),
        (FUND_UNCONDITIONAL, 'unconditional'),
    )

    #### Duration range for choices
    DURATION_CHOICES = zip( range(1, 31), range(1, 31) )

    desc_headline = models.CharField(_('Headline'), max_length=300)
    desc_preview = models.TextField(_('Short description'), max_length=400)
    summ_goal = models.PositiveIntegerField()
    duration = models.PositiveSmallIntegerField(choices=DURATION_CHOICES)
    image_main = models.ImageField(verbose_name=_('Campaign image'), blank=True, upload_to='campaigns_images')
    desc_main = models.TextField(_('Description'))
    collected_summ = models.PositiveIntegerField(blank=True, default=0)
    editors = models.ManyToManyField(ComeoUser, related_name='campaign_editors', verbose_name=_('campaign editors'))
    owner = models.ForeignKey(ComeoUser, verbose_name=_('campaign owner'), null=True)
    state = models.CharField(_('State'), max_length=50, choices=STATES, default=STATE_DRAFT)
    tags = models.ManyToManyField(Tag, verbose_name=_('Tags'), blank=True)
    funding_type = models.CharField(verbose_name=_('Funding type'), max_length=50, choices=FUND_TYPES, default=FUND_UNCONDITIONAL)
    date_start = models.DateField(_('start date'), null=True)
    date_finish = models.DateField(_('finish date'), null=True)
    date_created = models.DateTimeField(_('creation date'), default=timezone.now)
    views_count = models.PositiveIntegerField(_('view count'), default=0)




    def income_transaction(self, transaction):

        # TODO: campaign sum can be incremented by the same transaction twice.
        # TEST neded: ope campaign recieves the same transaction twice, summ shoul not be incresead in this case,
        #  it shoudl be equal to summ saved before transaction sent to campaign second time


        self.collected_summ += transaction.amount
        self.save()

    # def get_progress_percents(self):
    #     percents = (self.collected_summ*100)/self.summ_goal
    #     return int(round(percents))

    def days_to_finish(self):
        now = timezone.now().date()
        if self.date_finish:
            days_left = self.date_finish - now
            return days_left.days


class Transaction(models.Model):

    METHOD_CARD = 'METHOD_CARD'
    METHOD_TERMINAL = 'METHOD_TERMINAL'

    PAYMENT_METHODS = (
        (METHOD_CARD, 'Bank card'),
        (METHOD_TERMINAL, 'Terminal'),
    )

    amount = models.PositiveSmallIntegerField()
    method = models.CharField(choices=PAYMENT_METHODS, default=METHOD_CARD, max_length=40)
    campaign = models.ForeignKey(Campaign)
    payer = models.ForeignKey(ComeoUser)
    external_id = models.CharField(max_length=150, null=True)
    date_created = models.DateTimeField(default=timezone.now)
    confirmed = models.BooleanField(default=False) # transaction is confirmed by successful callback from payment partner
    date_confirmed = models.DateTimeField(null=True)

    def confirm(self):
        self.campaign.income_transaction(self)
        self.date_confirmed = timezone.now()
        self.confirmed = True
        self.save()
