#!/usr/bin/python3
""" BasicCache module
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache inherits from BaseCaching and implements
    a basic caching system with no limit
    """

    def put(self, key, item):
        """ Add an item to the cache
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item from the cache
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
