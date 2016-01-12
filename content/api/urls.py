from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

from .views import CategoryViewSet, ContentFeedViewSet, FeedArticleViewSet

router = routers.DefaultRouter()
router.register(r'categories', CategoryViewSet, base_name="category")
router.register(r'feeds', ContentFeedViewSet)
router.register(r'articles', FeedArticleViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
