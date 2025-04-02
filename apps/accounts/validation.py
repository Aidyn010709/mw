from django.core.validators import RegexValidator
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _


@deconstructible
class PhoneNumberValidator(RegexValidator):
    """
        Валидация телефона
    """
    regex = r"^\+\d+$"
    message = _("Номер Телефоа должен начинаться с '+' и с цифр")
    flags = 0
