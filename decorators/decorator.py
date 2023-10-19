import functools
from datetime import time
from heapq import nsmallest
from operator import itemgetter
import collections



# 1. Реалізувати LFU алгоритм для кешування.
# За базу берем існуючий декоратор.Написати для фетчування юерелів.
# Додати можливість указати максимум елементів в кеші.


def lfu_cache(max_limit=100):
    '''Least-frequenty-used cache decorator. '''
    counter = {}
    def internal(f):
        cache = {}  # mapping of args to results
        use_count = counter  # times each cache_key has been accessed
        kwd_mark = object()  # separate positional and keyword args

        @functools.wraps(f)
        def deco(*args, **kwargs):
            cache_key = args
            if kwargs:
                cache_key += (kwd_mark,) + tuple(sorted(kwargs.items()))
            use_count[cache_key] += 1

            # get cache entry or compute if not found
            try:
                result = cache[cache_key]
                deco.hits += 1
            except KeyError:
                result = f(*args, **kwargs)
                cache[cache_key] = result
                deco.misses += 1

                # Clear the least frequently used cache entry
                if len(cache) > max_limit:
                    for cache_key, _ in nsmallest(max_limit,
                                                  use_count.items(),
                                                  key=itemgetter(1)):
                        del cache[cache_key], use_count[cache_key]

            return result

        def clear():
            cache.clear()
            use_count.clear()
            deco.hits = deco.misses = 0

        deco.hits = deco.misses = 0
        deco.clear = clear
        return deco
    return internal

