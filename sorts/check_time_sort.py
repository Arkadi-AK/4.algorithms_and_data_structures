import random
import time

from sorts.merge_sort import merge_sort
from sorts.quick_sort import quickSort, quick_sort

array = [random.randint(1, 100) for i in range(100000)]


def timer(func):
    def inner(*args, **kwargs):
        start_time = time.time()
        rez = func(*args, **kwargs)
        end_time = time.time() - start_time
        print(f"Функция {func.__name__} отработала за: {end_time} seconds")
        return rez

    return inner


python_sort = sorted
python_sort = timer(python_sort)
python_sort(array)

merge_sort = timer(merge_sort)
merge_sort(array)

quickSort = timer(quickSort)
quickSort(array)

quick_sort = timer(quick_sort)
quick_sort(array)
