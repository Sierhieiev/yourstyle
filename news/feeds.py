# -*- coding: utf-8 -*-
from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Atom1Feed
from news.models import Post

class RssLatestPosts(Feed):
    title = u"Останні новини"
    link = "/news/"
    description = u"Останні новини нашого сайту!"

    def items(self):
        return Post.objects.order_by('-post_date')[:5]
    def item_description(self, item):
        return item.get_preview().rstrip()

class AtomLatestPosts(RssLatestPosts):
    feed_type = Atom1Feed
    subtitle = RssLatestPosts.description