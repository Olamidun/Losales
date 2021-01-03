from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.

class AccountManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password=None):
        if first_name is None:
            raise TypeError('First name cannot be empty')
        if last_name is None:
            raise TypeError('Last name cannot be empty')
        if email is None:
            raise TypeError('Users should have an email address')
        user = self.model(
            first_name=first_name,
            last_name=last_name,
            email=self.normalize_email(email)
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, password):
        user = self.create_user(email, first_name, last_name, password)
        user.is_superuser = True
        user.is_active = True
        user.is_staff = True
        user.is_admin = True
        user.is_verified = True
        user.save(using=self._db)
        return user

    
class Account(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=255, unique=True)
    is_verified = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_dispatch_rider = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = AccountManager()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


# class DispatchRiderManager(BaseUserManager):
#     def create_dispatch_rider(self, email, full_name, country, password):
#         if full_name is None:
#             raise TypeError('Last name cannot be empty')
#         if email is None:
#             raise TypeError('Users should have an email address')
#         if country is None:
#             raise TypeError('Users should have an email address')
#         user = self.model(
#             full_name=full_name,
#             country=country,
#             email=self.normalize_email(email)
#         )

#         user.set_password(password)
#         user.save(using=self._db)
#         return user    


# class DispatchRider(AbstractBaseUser, PermissionsMixin):
#     full_name = models.CharField(max_length=200)
#     email = models.EmailField(max_length=255, unique=True)
#     country = models.CharField(max_length=30)
#     is_verified = models.BooleanField(default=False)
#     is_admin = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=False)
#     is_staff = models.BooleanField(default=False)
#     is_dispatch_rider = models.BooleanField(default=True)
#     date_joined = models.DateTimeField(auto_now_add=True)

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['full_name', 'country']

#     objects = DispatchRiderManager()

#     def __str__(self):
#         return f'{self.full_name}'
