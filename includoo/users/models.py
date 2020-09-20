from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, BooleanField, IntegerChoices, TextChoices
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """Default user for includoo."""

    class TimeOfMeeting(TextChoices):
        LUNCH = 'L', _('LUNCH')
        WEEKDAY = 'WD', _('WEEKDAY')
        WEEKEND = 'WE', _('WEEKEND')

    class PlaceOfMeeting(TextChoices):
        VIRTUAL = 'V', _('VIRTUAL')
        PHYSICAL = 'P', _('PHYSICAL')

    #: First and last name do not cover name patterns around the globe
    name = CharField(_("Name of User"), blank=True, max_length=255)
    time = CharField(max_length=2, choices=TimeOfMeeting.choices, default=TimeOfMeeting.WEEKDAY)
    place = CharField(max_length=1, choices=PlaceOfMeeting.choices, default=PlaceOfMeeting.VIRTUAL)
    interest_sports = BooleanField(_("Sports"), default=0, blank=True)
    interest_arts = BooleanField(_("Arts"), default=0, blank=True)
    interest_social = BooleanField(_("Social"), default=0, blank=True)
    interest_env = BooleanField(_("Env"), default=0, blank=True)
    interest_drinks = BooleanField(_("Drinks"), default=0, blank=True)
    interest_startups = BooleanField(_("Startups"), default=0, blank=True)
    interest_games = BooleanField(_("Games"), default=0, blank=True)
    interest_photography = BooleanField(_("Photography"), default=0, blank=True)

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})
