from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractUser, BaseUserManager
from domains.models import Domain

class UserManager(BaseUserManager):
    """
    User manager for handling email as username.
    """

    def create_user(self, email, password=None, **kwargs):
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **kwargs):
        user = self.model(email=email, is_staff=True, is_superuser=True, **kwargs)
        user.set_password(password)
        user.save()
        return user


class User(AbstractUser):
    """
    Our own user model uses email as the main field and skips usernames entirely.
    """
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    username = None
    domain = models.ForeignKey(Domain)
    email = models.EmailField(_('Email address'), blank=False, unique=True)
    objects = UserManager()
    quota = models.IntegerField(default=0)
    active = models.BooleanField(default=True)
