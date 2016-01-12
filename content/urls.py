from django.conf.urls import url, include
from .views import update_feeds

urlpatterns = [
    url(r'^update/?$', update_feeds, name="update_feeds"),
]
