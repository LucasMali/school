import random

def mergeSort(list_of_items, split_by_3=False):
    """MergeSort one method.
    
    This is not optimize nor is it recommend for real world scenerios. This was only for
    learning exercises.
    
    Also, this might not be 100% accurate to the behavior of how merge sort is supposed to run when spliting by 3.
    

    Args:
        list_of_items ([type]): [description]
        split_by_3 (bool, optional): [description]. Defaults to False.

    Returns:
        [type]: [description]
    """
    # Use a breakpoint in the code line below to debug your script.
    run = True
    split_it = 3 if split_by_3 else 2
    items_len = len(list_of_items)
    split = items_len // split_it

    # Swapping logic.
    # NOTE: This condition might be better using split_by_3 flag to dictate behavior.
    if split < 1 and items_len > 1:  
        swapped = True
        index = 0
        while swapped:
            swapped = False
            list_len = len(list_of_items)

            for i in list_of_items:
                next_index = index + 1
                if next_index > list_len-1:
                    swapped = True
                elif i > list_of_items[next_index]:
                    list_of_items[index], list_of_items[next_index] = list_of_items[next_index], list_of_items[index]
                    swapped = True

                index = next_index if list_len-1 > next_index else 0
    elif split > 0:
        if split_by_3:
            a = list_of_items[:split]
            b = list_of_items[split:-split]
            c = list_of_items[-split:]
            t = [
                mergeSort(list_of_items[:split], split_by_3),
                mergeSort(list_of_items[split:-split], split_by_3),
                mergeSort(list_of_items[-split:], split_by_3)
            ]
        else:
            a = list_of_items[:split]
            c = list_of_items[split:]
            t = [
                mergeSort(list_of_items[:split], split_by_3),
                mergeSort(list_of_items[split:], split_by_3)
            ]

        # merge them
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

        # list
        list_of_items = tmp

    return list_of_items

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # generate random nubmers
    print("Testing with even array")
    item_arr = [101, 43, 4, 5, 68, 6, 1, 9, 100, 20, 33, 22, 88, 3]
    final = [1, 3, 4, 5, 6, 9, 20, 22, 33, 43, 68, 88, 100, 101]

    item_arr = mergeSort(item_arr)
    print(item_arr)
    assert item_arr == final

    item_arr = mergeSort(item_arr, True)
    print(item_arr)
    assert item_arr == final

    print("Testing with odd array")
    item_arr = [101, 43, 4, 5, 68, 6, 1, 9, 100, 20, 33, 22, 88]
    final = [1, 4, 5, 6, 9, 20, 22, 33, 43, 68, 88, 100, 101]

    item_arr = mergeSort(item_arr)
    print(item_arr)
    assert item_arr == final

    item_arr = mergeSort(item_arr, True)
    print(item_arr)
    assert item_arr == final

    print("Testing with small odd array")
    item_arr = [101, 43, 4]
    final = [4, 43, 101]

    item_arr = mergeSort(item_arr)
    print(item_arr)
    assert item_arr == final

    item_arr = mergeSort(item_arr, True)
    print(item_arr)
    assert item_arr == final

    print("Testing with small even array")
    item_arr = [101, 43, 4, 1]
    final = [1, 4, 43, 101]

    item_arr = mergeSort(item_arr)
    print(item_arr)
    assert item_arr == final

    item_arr = mergeSort(item_arr, True)
    print(item_arr)
    assert item_arr == final

    print("Testing with two")
    item_arr = [101, 43]
    final = [43, 101]

    item_arr = mergeSort(item_arr)
    print(item_arr)
    assert item_arr == final

    item_arr = mergeSort(item_arr, True)
    print(item_arr)
    assert item_arr == final

    print("Testing with one")
    item_arr = [101]
    final = [101]

    item_arr = mergeSort(item_arr)
    print(item_arr)
    assert item_arr == final

    item_arr = mergeSort(item_arr, True)
    print(item_arr)
    assert item_arr == final

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

    item_arr = mergeSort(item_arr)
    print(item_arr)
    assert item_arr == final

    item_arr = mergeSort(item_arr, True)
    print(item_arr)
    assert item_arr == final