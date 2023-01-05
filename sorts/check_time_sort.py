import random
import time

from sorts.merge_sort import merge_sort

array = [random.randint(1, 100) for i in range(10000)]


def timer(func):
    def inner(*args, **kwargs):
        start_time = time.time()
        rez = func(*args, **kwargs)
        end_time = time.time() - start_time
        print(f"Функция {func.__name__} отработала за: {end_time} seconds")
        return rez

    return inner


merge_sort = timer(merge_sort)
merge_sort(array)
