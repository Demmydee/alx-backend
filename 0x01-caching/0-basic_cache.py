#!/usr/bin/env python3

"""
Basic dictionary
"""


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Inherits from `BaseCaching`mand is a caching system
    """

    def put(self, key, item):
        """
        Assigns to the dictionary `self.cache_data` the
           `item` value for the key `key`
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Returns the value in `self.cache_data` linked to `key`
        """

        return self.cache_data.get(key, None)
