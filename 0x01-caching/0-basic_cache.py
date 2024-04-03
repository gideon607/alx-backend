#!/usr/bin/python3

""" This is a Basic Dictionary """

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Basic dictionary function"""

    def put(self, key, item):
        """Puts items in cache"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Gets items from cache"""
        return self.cache_data.get(key, None)
