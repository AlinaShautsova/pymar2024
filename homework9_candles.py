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


assert solution(5, 2) == 9, \
    "Function with input values 5 and 2, not equal 9."
assert solution(1, 2) == 1, \
    "Function with input values 1 and 2, not equal 1."
assert solution(15, 5) == 18, \
    "Function with input values 15 and 5, not equal 18."
assert solution(12, 2) == 23, \
    "Function with input values 12 and 2, not equal 23."
assert solution(6, 4) == 7, \
    "Function with input values 6 and 4, not equal 7."
assert solution(13, 5) == 16, \
    "Function with input values 13 and 5, not equal 16."
assert solution(2, 3) == 2, \
    "Function with input values 2 and 3, not equal 2."
