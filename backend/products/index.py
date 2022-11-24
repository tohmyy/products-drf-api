# index.py

# from dataclasses import fields

from algoliasearch_django import AlgoliaIndex
from algoliasearch_django.decorators import register
# import algoliasearch_django as algoliasearch



from .models import Product

# algoliasearch.register(Product)

@register(Product)
class ProductIndex(AlgoliaIndex):
    should_index = 'is_public'
    fields=[
        'title',
        'content',
        'price',
        'user',
        'public',
        'path',
    ]

    settings = {
        'searchableAttributes': ['title', 'content', 'price'],
        'attributesForFaceting': ['user', 'public']
    }

    tags='get_tags_list'
