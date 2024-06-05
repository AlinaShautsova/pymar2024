"""Module providing a function printing python version."""


def solution(number_of_candles, number_of_leftovers):
    """Create new candles from the leftovers and count the
    total number of candles and write down the answer."""
    answer = number_of_candles
    leftovers = number_of_candles

    while leftovers >= number_of_leftovers:
        new_candles = leftovers // number_of_leftovers
        answer += new_candles
        leftovers = leftovers % number_of_leftovers + new_candles

    return answer


assert solution(5, 2) == 9
assert solution(1, 2) == 1
assert solution(15, 5) == 18
assert solution(12, 2) == 23
assert solution(6, 4) == 7
assert solution(13, 5) == 16
assert solution(2, 3) == 2
