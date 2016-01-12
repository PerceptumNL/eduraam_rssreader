from rest_framework import serializers, viewsets
from content.models import Category, ContentFeed, FeedArticle
from rest_framework.decorators import detail_route
from rest_framework.response import Response

class FeedArticleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FeedArticle
        fields = ('id', 'url', 'publication_date',
                'title','body', 'image', 'categories')


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    articles = FeedArticleSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ('id', 'url', 'title', 'color', 'order', 'image', 'articles')


class ContentFeedSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ContentFeed
        fields = ('id', 'feed', 'last_update', 'category')


class FeedArticleViewSet(viewsets.ModelViewSet):
    queryset = FeedArticle.objects.all()
    serializer_class = FeedArticleSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ContentFeedViewSet(viewsets.ModelViewSet):
    queryset = ContentFeed.objects.all()
    serializer_class = ContentFeedSerializer

