from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProfileViewSet, UpdateProfileView, DeleteProfileView

router = DefaultRouter()
router.register(r'profiles', ProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('profiles/update/', UpdateProfileView.as_view(), name='profile-update'),
    path('profiles/delete/', DeleteProfileView.as_view(), name='profile-delete'),
]
