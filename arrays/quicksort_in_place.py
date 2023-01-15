from typing import List


'''
Implement quicksort_in_place
'''


Vector = List[int]


def quicksort_in_place(l: Vector, low: int = 0, high: int = None) -> Vector:
    if not high:
        high = len(l) - 1
    if high < 0 or high - low < 1:
        return
    # keep track of the current subarray we're sorting
    top = high
    bottom = low
    # choose the first element as the pivot
    pivot_index = low
    pivot_value = l[pivot_index]
    # start our index with the next element
    index = low + 1
    while low < high:
        if l[index] < pivot_value:  # if the value is less swap the item to be before the pivot
            l[index], l[pivot_index] = l[pivot_index], l[index]
            pivot_index = index
            index += 1
            low += 1
        elif l[index] == pivot_index:  # if the value is the same as the pivot, move to the next
            index += 1
        else:  # otherwise, the value is higher, move it to the end of the unsorted region
            l[index], l[high] = l[high], l[index]
            high -= 1
    quicksort_in_place(l, bottom, pivot_index - 1)
    quicksort_in_place(l, pivot_index + 1, top)
    return l

if __name__ == '__main__':
    test = [5, 2, 6, 0, 8, 7, 3, 9, 1, 4]
    desired = list(range(10))
    result = quicksort_in_place(test)
    try:
        assert result == desired
    except AssertionError:
        print(f'{result} is not equal to {desired}')
    else:
        print('You got it!')

    test = [5, 8, 2, 6, 5, 0, 7, 3, 9, 1]
    desired = [0, 1, 2, 3, 5, 5, 6, 7, 8, 9]
    result = quicksort_in_place(test, 0)
    try:
        assert result == desired
    except AssertionError:
        print(f'{result} is not equal to {desired}')
    else:
        print('You got it!')