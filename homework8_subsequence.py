"""Module providing a function printing python version."""


def test_for_increasing_function(arr):
    """Testing for increasing function."""
    for i in range(len(arr) - 1):
        if arr[i] >= arr[i + 1]:
            return False
    return True


def will_it_be_strictly_increasing(arr):
    """The function slices through and checks on increasing."""
    if test_for_increasing_function(arr):
        return True

    for i in range(len(arr)):
        new_arr = arr[:i] + arr[i + 1:]
        if test_for_increasing_function(new_arr):
            return True
    return False


def solution(arr):
    """Response output."""
    return will_it_be_strictly_increasing(arr)


assert solution([1, 2, 3])
assert solution([1, 2, 1, 2])
assert solution([1, 3, 2, 1])
assert solution([1, 2, 3, 4, 5, 3, 5, 6])
assert solution([40, 50, 60, 10, 20, 30])
