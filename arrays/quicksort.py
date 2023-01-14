from typing import List


'''
Implement quicksort
'''


Vector = List[int]


def quicksort(l: Vector) -> Vector:
    if len(l) < 2:
        return l
    pivot_index = int(len(l) / 2)
    pivot_value = l[pivot_index]
    left = []
    right = []
    for i, v in enumerate(l):
        if i == pivot_index:
            continue
        if v < pivot_value:
            left.append(v)
        else:
            right.append(v)
    return quicksort(left) + [pivot_value] + quicksort(right)


if __name__ == '__main__':
    test = [0, 8, 2, 6, 4, 5, 7, 3, 9, 1]
    desired = list(range(10))
    result = quicksort(test)
    try:
        assert result == desired
    except AssertionError:
        print(f'{result} is not equal to {desired}')
    else:
        print('You got it!')

    test = [0, 8, 2, 6, 5, 5, 7, 3, 9, 1]
    desired = [0, 1, 2, 3, 5, 5, 6, 7, 8, 9]
    result = quicksort(test)
    try:
        assert result == desired
    except AssertionError:
        print(f'{result} is not equal to {desired}')
    else:
        print('You got it!')