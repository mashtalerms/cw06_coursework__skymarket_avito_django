from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.core.validators import EmailValidator
from django.db import models
from .managers import UserManager
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _


class UserRoles:
    USER = "user"
    ADMIN = "admin"
    ROLE = [(USER, USER), (ADMIN, ADMIN)]


class User(AbstractBaseUser):

    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20, blank=True, null=True)
    last_name = models.CharField(max_length=20, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(null=True, blank=True, unique=True, validators=[EmailValidator])
    role = models.CharField(choices=UserRoles.ROLE, max_length=9, default=UserRoles.USER, null=True, blank=True)
    image = models.ImageField(upload_to="user_avatars/", null=True, blank=True)
    is_active = models.BooleanField(default=False, null=True)

    class Meta:
        verbose_name = _("Пользователь")
        verbose_name_plural = _("Пользователи")
        ordering = ['email']

    def __str__(self):
        return self.email

    # эта константа определяет поле для логина пользователя
    USERNAME_FIELD = "email"

    # эта константа содержит список с полями,
    # которые необходимо заполнить при создании пользователя
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone']

    objects = UserManager()

    @property
    def is_admin(self):
        return self.role == UserRoles.ADMIN

    @property
    def is_user(self):
        return self.role == UserRoles.USER

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin
