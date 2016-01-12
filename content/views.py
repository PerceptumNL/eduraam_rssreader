from django.http import HttpResponse
from .models import ContentFeed

def update_feeds(request):
    for feed in ContentFeed.objects.all():
        feed.update_feed()
    return HttpResponse(status=204)
