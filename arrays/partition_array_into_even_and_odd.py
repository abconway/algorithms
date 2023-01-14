from typing import List


'''
Given an array of N elements, reorder the elements so that the even elements appear first.
Do so without allocating additional storage.
'''


Vector = List[int]


def partition(l: Vector) -> Vector:
    even_index = 0
    odd_index = len(l) - 1
    while even_index < odd_index:
        if l[even_index] % 2 == 0:
            even_index += 1
        else:
            l[even_index], l[odd_index] = l[odd_index], l[even_index]
            odd_index -= 1
    return l


if __name__ == '__main__':
    test = list(range(10))
    desired = [0, 8, 2, 6, 4, 5, 7, 3, 9, 1]
    result = partition(test)
    try:
        assert result == desired
    except AssertionError:
        print(f'{result} is not equal to {desired}')
    print('You got it!')
