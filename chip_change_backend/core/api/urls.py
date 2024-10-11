from django.urls import path, include
from rest_framework.routers import DefaultRouter
from ..views import UserViewSet, TransactionViewSet, AnnouncementViewSet, PointsHistoryViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'transactions', TransactionViewSet)
router.register(r'announcements', AnnouncementViewSet)
router.register(r'points-history', PointsHistoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
