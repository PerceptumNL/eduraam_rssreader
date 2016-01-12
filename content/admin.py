from django.contrib import admin
from polymorphic.admin import PolymorphicParentModelAdmin, \
        PolymorphicChildModelAdmin
from .models import Category, ContentFeed, KidsWeekFeed, SevenDaysFeed, \
        RSSFeed, FeedArticle

class RSSFeedAdmin(PolymorphicChildModelAdmin):
    base_model = RSSFeed

class KidsWeekFeedAdmin(PolymorphicChildModelAdmin):
    base_model = KidsWeekFeed

class SevenDaysFeedAdmin(PolymorphicChildModelAdmin):
    base_model = SevenDaysFeed

class ContentFeedAdmin(PolymorphicParentModelAdmin):
    base_model = ContentFeed
    child_models = (
        (RSSFeed, RSSFeedAdmin),
        (KidsWeekFeed, KidsWeekFeedAdmin),
        (SevenDaysFeed, SevenDaysFeedAdmin)
    )

admin.site.register(Category)
admin.site.register(FeedArticle)
admin.site.register(ContentFeed, ContentFeedAdmin)
