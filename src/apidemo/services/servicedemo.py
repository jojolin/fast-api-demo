"""
service demo
"""
from functools import lru_cache

"""
add lru_cache make the __init__ to be call only once
"""


@lru_cache()
class ServiceDemo(object):

    def __init__(self):
        self.info = 'call __init__'
        print(self.info)

    @lru_cache()
    def initialize(self):
        print('call initialize')
