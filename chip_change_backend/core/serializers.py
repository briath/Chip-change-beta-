from rest_framework import serializers
from .models import User, Transaction, Announcement, PointsHistory

# Сериализатор для модели User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'is_active', 'is_staff', 'created_at', 'updated_at', 'two_factor_enabled', 'social_id', 'points']

# Сериализатор для модели Transaction
class TransactionSerializer(serializers.ModelSerializer):
    seller = UserSerializer(read_only=True)
    buyer = UserSerializer(read_only=True)

    class Meta:
        model = Transaction
        fields = ['id', 'seller', 'buyer', 'amount', 'status', 'created_at', 'updated_at', 'points_awarded']

# Сериализатор для модели Announcement
class AnnouncementSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Announcement
        fields = ['id', 'user', 'chips_amount', 'rate', 'min_volume', 'payment_method', 'created_at', 'updated_at']

# Сериализатор для модели PointsHistory
class PointsHistorySerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    transaction = TransactionSerializer(read_only=True)

    class Meta:
        model = PointsHistory
        fields = ['id', 'user', 'transaction', 'points', 'reason', 'created_at']
