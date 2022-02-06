import random

def mergeSortMicroSort(list_of_items: list) -> list:
    swapped = True
    index = 0
    while swapped:
        swapped = False
        list_len = len(list_of_items)

        for i in list_of_items:
            next_index = index + 1
            if next_index > list_len - 1:
                swapped = True
            elif i > list_of_items[next_index]:
                list_of_items[index], list_of_items[next_index] = list_of_items[next_index], list_of_items[index]
                swapped = True

            index = next_index if list_len - 1 > next_index else 0

    return list_of_items

def mergeSortMicroMerge(t: list)->list:
    run = True
    tmp = []
    cursor = 0

    while run:
        if not len(t[cursor]) and not len(t[cursor + 1]):
            cursor += 1
            run = False if cursor >= len(t) - 1 else True
            if run:
                t[cursor] = tmp
                tmp = []
        elif not len(t[cursor]) and len(t[cursor + 1]):
            tmp.append(t[cursor + 1].pop(0))
        elif not len(t[cursor + 1]) and len(t[cursor]):
            tmp.append(t[cursor].pop(0))
        elif t[cursor][0] < t[cursor + 1][0]:
            tmp.append(t[cursor].pop(0))
        else:
            tmp.append(t[cursor + 1].pop(0))

    return tmp

def mergeSortSplit(list_of_items: list, split_by_3: bool) -> list:
    split_it = 3 if split_by_3 else 2
    items_len = len(list_of_items)
    split = items_len // split_it

    if split == 0 and items_len <= 1:
        return list_of_items

    if split == 1 and split_it == 2 and items_len <= split_it:
        return mergeSortMicroSort(list_of_items)

    if split == 0 and items_len > 1:
        return mergeSortMicroSort(list_of_items)

    if split_by_3:
        i = split
        j = split*2
        a = list_of_items[:i]
        b = list_of_items[i:j]
        c = list_of_items[j:]
        aa = list_of_items[:split]
        bb = list_of_items[split:-split]
        cc = list_of_items[-split:]
        pause = True
        t = [
            mergeSortSplit(list_of_items[:i], split_by_3),
            mergeSortSplit(list_of_items[i:j], split_by_3),
            mergeSortSplit(list_of_items[j:], split_by_3)
        ]
    else:
        a = list_of_items[:split]
        c = list_of_items[split:]
        t = [
            mergeSortSplit(list_of_items[:split], split_by_3),
            mergeSortSplit(list_of_items[split:], split_by_3)
        ]

    # merge them
    list_of_items = mergeSortMicroMerge(t)

    # list
    return list_of_items

def mergeSort(list_of_items, split_by_3=False):
    list_of_items = mergeSortSplit(list_of_items, split_by_3)
    return list_of_items

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # generate random nubmers
    print("Testing with even array")
    item_arr = [101, 43, 4, 5, 68, 6, 1, 9, 100, 20, 33, 22, 88, 3]
    final = item_arr.copy()
    final.sort()

    print(mergeSort(item_arr))
    assert mergeSort(item_arr) == final

    print(mergeSort(item_arr, True))
    assert mergeSort(item_arr, True) == final

    print("Testing with odd array")
    item_arr = [101, 43, 4, 5, 68, 6, 1, 9, 100, 20, 33, 22, 88]
    final = item_arr.copy()
    final.sort()

    print(mergeSort(item_arr))
    assert mergeSort(item_arr) == final

    print(mergeSort(item_arr, True))
    assert mergeSort(item_arr, True) == final

    print("Testing with small odd array")
    item_arr = [101, 43, 4]
    final = item_arr.copy()
    final.sort()

    print(mergeSort(item_arr))
    assert mergeSort(item_arr) == final

    print(mergeSort(item_arr, True))
    assert mergeSort(item_arr, True) == final

    print("Testing with small even array")
    item_arr = [101, 43, 4, 1]
    final = item_arr.copy()
    final.sort()

    print(mergeSort(item_arr))
    assert mergeSort(item_arr) == final

    print(mergeSort(item_arr, True))
    assert mergeSort(item_arr, True) == final

    print("Testing with two")
    item_arr = [101, 43]
    final = item_arr.copy()
    final.sort()

    print(mergeSort(item_arr))
    assert mergeSort(item_arr) == final

    print(mergeSort(item_arr, True))
    assert mergeSort(item_arr, True) == final

    print("Testing with one")
    item_arr = [101]
    final = item_arr.copy()
    final.sort()

    print(mergeSort(item_arr))
    assert mergeSort(item_arr) == final

    print(mergeSort(item_arr, True))
    assert mergeSort(item_arr, True) == final

    print("Random dynamic stuff")
    index = 0
    random_length = random.randint(100,10000)
    item_arr = []
    while index < random_length:
        num = random.randint(1,100000)
        if num in item_arr:
            continue
        item_arr.append(num)
        index += 1

    final = item_arr.copy()
    final.sort()

    print(mergeSort(item_arr))
    assert mergeSort(item_arr) == final

    print(mergeSort(item_arr, True))
    assert mergeSort(item_arr, True) == final



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
