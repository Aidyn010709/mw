from django.db import models
from django.utils.translation import gettext_lazy as _


class Role(models.TextChoices):
    USER = "customuser", _("Пользователь")
    DIRECTOR = "director", _("Директор")
    ADMIN = "admin", _("Админ")
