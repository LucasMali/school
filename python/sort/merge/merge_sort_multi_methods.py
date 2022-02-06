import random

def mergeSortMicroSort(list_of_items: list):
    """Merge Sort Micro Sort.

    This is the simple sorting of smallest to largest.

    Args:
        list_of_items (list): Contains the list of numeric items

    Returns:
        list: The sorted items
    """
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
                list_of_items[index], list_of_items[next_index] = (
                    list_of_items[next_index],
                    list_of_items[index],
                )
                swapped = True

            index = next_index if list_len - 1 > next_index else 0

    return list_of_items


def mergeSortMicroMerge(lists_to_be_merged: list):
    """Merge Sort Micro Merge.

    This is a merge helper, as the recursive values merge back into eachother.

    Args:
        lists_to_be_merged (list): List of lists with numeric values.

    Returns:
        list : List of numeric values in ascending order.
    """
    run_merge = True
    new_compiled_list = []
    cursor = 0

    while run_merge:
        if not len(lists_to_be_merged[cursor]) and not len(lists_to_be_merged[cursor + 1]):
            cursor += 1
            run_merge = False if cursor >= len(lists_to_be_merged) - 1 else True
            if run_merge:
                lists_to_be_merged[cursor] = new_compiled_list
                new_compiled_list = []
        elif not len(lists_to_be_merged[cursor]) and len(lists_to_be_merged[cursor + 1]):
            new_compiled_list.append(lists_to_be_merged[cursor + 1].pop(0))
        elif not len(lists_to_be_merged[cursor + 1]) and len(lists_to_be_merged[cursor]):
            new_compiled_list.append(lists_to_be_merged[cursor].pop(0))
        elif lists_to_be_merged[cursor][0] < lists_to_be_merged[cursor + 1][0]:
            new_compiled_list.append(lists_to_be_merged[cursor].pop(0))
        else:
            new_compiled_list.append(lists_to_be_merged[cursor + 1].pop(0))

    return new_compiled_list


def mergeSortSplit(list_of_items: list, split_by_3: bool):
    """Merge Sort Split.

    Here is where we use recursion to break down the list of numbers given.

    Args:
        list_of_items (list): List of numeric values.
        split_by_3 (bool): Split by 2 or 3 sections?

    Returns:
        list: List of numeric values in ascending order.
    """
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
        t = [
            mergeSortSplit(list_of_items[:split], split_by_3),
            mergeSortSplit(list_of_items[split: split * 2], split_by_3),
            mergeSortSplit(list_of_items[split * 2:], split_by_3),
        ]
    else:
        t = [
            mergeSortSplit(list_of_items[:split], split_by_3),
            mergeSortSplit(list_of_items[split:], split_by_3),
        ]
    # merge them
    return mergeSortMicroMerge(t)

def mergeSort(list_of_items, split_by_3=False):
    list_of_items = mergeSortSplit(list_of_items, split_by_3)
    return list_of_items

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
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
