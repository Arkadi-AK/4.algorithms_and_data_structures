def quickSort(array):
    array = array[:]
    if len(array) > 1:
        pivot = array.pop()
        grtr_lst, equal_lst, smlr_lst = [], [pivot], []
        for item in array:
            if item == pivot:
                equal_lst.append(item)
            elif item > pivot:
                grtr_lst.append(item)
            else:
                smlr_lst.append(item)
        return (quickSort(smlr_lst) + equal_lst + quickSort(grtr_lst))
    else:
        return array


def quick_sort(array):
    if len(array) <= 1:
        return array
    elem = array[0]
    left = list(filter(lambda x: x < elem, array))
    center = [i for i in array if i == elem]  # Вариант исп. list comprehension
    right = list(filter(lambda x: x > elem, array))
    return quick_sort(left) + center + quick_sort(right)
