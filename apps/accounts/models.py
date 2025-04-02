from django.contrib.auth.models import AbstractUser, BaseUserManager
from apps.accounts.validation import PhoneNumberValidator
from django.utils.translation import gettext_lazy as _
from utils.constants import Role
from django.db import models


class UserManager(BaseUserManager):
    """
    Custom user model manager where phone_number is the unique identifier
    for authentication.
    """

    def create_user(self, email, phone_number=None, password=None, **extra_fields):
        """
        Create and save a User with the given phone_number and password.
        """
        user = self.model(email=email, phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, phone_number=None, password=None, **extra_fields):
        """
        Create and save a SuperUser with the given phone_number and password.
        """
        user = self.create_user(email, phone_number, password, **extra_fields)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractUser):
    phone_number_validator = PhoneNumberValidator()

    phone_number = models.CharField(
        verbose_name=_("Номер телефона"),
        unique=True,
        max_length=13,
        help_text=_(
            "Обязательное поле. Должно содержать от 10 цифр (0700 123 456) до 12 цифр (+996 700 123 456"
        ),
        validators=[phone_number_validator],
        error_messages={
            "unique": _("Пользователь с таким номером телефона уже существует."),
        },
        blank=True,
        null=True
    )
    first_name = models.CharField(_("first name"), max_length=150, blank=True)
    last_name = models.CharField(_("last name"), max_length=150, blank=True)
    email = models.EmailField(verbose_name="Электронная почта", unique=True)
    code = models.CharField(max_length=5, verbose_name="Код для подтвеждение")
    role = models.CharField(
        max_length=50,
        choices=Role,
        default='customer',
        verbose_name="Роль пользователя"
    )
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone_number']

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

        constraints = [
            models.UniqueConstraint(
                fields=["phone_number"],
                name="unique_phone",
            )
        ]

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.get_role_display()})"

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = f"{self.first_name} {self.last_name}"
        return full_name.strip()
