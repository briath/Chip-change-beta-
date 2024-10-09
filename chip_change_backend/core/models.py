from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils import timezone

# Менеджер пользователей
class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)

# Модель пользователя
class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    two_factor_enabled = models.BooleanField(default=False)
    social_id = models.CharField(max_length=255, null=True, blank=True)
    points = models.IntegerField(default=0)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

# Модель транзакций
class Transaction(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='seller_transactions')
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='buyer_transactions')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    points_awarded = models.IntegerField(default=0)

    def __str__(self):
        return f"Transaction {self.id} - {self.status}"

# Модель объявлений
class Announcement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='announcements')
    chips_amount = models.IntegerField()
    rate = models.DecimalField(max_digits=10, decimal_places=2)
    min_volume = models.IntegerField()
    payment_method = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Announcement {self.id} by {self.user.email}"

# Модель истории начисления баллов
class PointsHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='points_history')
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE, null=True, blank=True, related_name='points_entries')
    points = models.IntegerField()
    reason = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"PointsHistory {self.id} - {self.user.email} ({self.points} points)"
