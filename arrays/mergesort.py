from typing import List


'''
Implement mergesort
'''


Vector = List[int]


def mergesort(l: Vector) -> Vector:
    if len(l) == 1:
        return l
    middle = int(len(l) / 2)
    left = l[:middle]
    right = l[middle:]
    left_sorted = mergesort(left)
    right_sorted = mergesort(right)
    left_index = 0
    right_index = 0
    sorted = []
    while left_index < len(left_sorted) or right_index < len(right_sorted):
        if left_index >= len(left_sorted):
            return sorted + right_sorted[right_index:]
        if right_index >= len(right_sorted):
            return sorted + left_sorted[left_index:]
        left_value = left_sorted[left_index]
        right_value = right_sorted[right_index]
        if left_value < right_value:
            sorted.append(left_value)
            left_index +=1
        else:
            sorted.append(right_value)
            right_index += 1
    return sorted


if __name__ == '__main__':
    test = [0, 8, 2, 6, 4, 5, 7, 3, 9, 1]
    desired = list(range(10))
    result = mergesort(test)
    try:
        assert result == desired
    except AssertionError:
        print(f'{result} is not equal to {desired}')
    else:
        print('You got it!')

    test = [0, 8, 2, 6, 5, 5, 7, 3, 9, 1]
    desired = [0, 1, 2, 3, 5, 5, 6, 7, 8, 9]
    result = mergesort(test)
    try:
        assert result == desired
    except AssertionError:
        print(f'{result} is not equal to {desired}')
    else:
        print('You got it!')