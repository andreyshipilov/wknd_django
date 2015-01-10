from django.core.urlresolvers import reverse, NoReverseMatch
from django.contrib.sitemaps import Sitemap
from sitetree.models import TreeItem
from sitetree.sitetreeapp import get_sitetree


sitetree = get_sitetree()


class TreeItemSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.8

    def items(self):
        return TreeItem.objects.filter(inmenu=True,).exclude(url__istartswith='http')

    def location(self, obj):
        try:
            url = reverse(obj.url)
        except NoReverseMatch:
            url = obj.url

        return url