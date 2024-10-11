from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import User, Transaction, Announcement, PointsHistory
from .serializers import UserSerializer, TransactionSerializer, AnnouncementSerializer, PointsHistorySerializer

# Представление для модели User
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

# Представление для модели Transaction
class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(seller=self.request.user)

# Представление для модели Announcement
class AnnouncementViewSet(viewsets.ModelViewSet):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# Представление для модели PointsHistory
class PointsHistoryViewSet(viewsets.ModelViewSet):
    queryset = PointsHistory.objects.all()
    serializer_class = PointsHistorySerializer
    permission_classes = [IsAuthenticated]
