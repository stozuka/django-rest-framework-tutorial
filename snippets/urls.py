from django.urls import path, include
from snippets.views import SnippetViewSet, UserViewSet, api_root
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'snippets', SnippetViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', api_root),
    path('', include(router.urls)),
]
