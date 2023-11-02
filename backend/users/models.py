from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """Represents a user that needs to be approved to login."""

    is_approved = models.BooleanField(default=False)
    first_name = models.CharField(verbose_name=_("First name"), max_length=150)
    last_name = models.CharField(verbose_name=_("Last name"), max_length=150)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.email
