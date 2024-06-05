"""Module providing a function printing python version."""


def solution(a):
    """Delete # and the symbol in front of it."""
    answer = []
    for s_for_delete in a:
        if s_for_delete != "#":
            answer.append(s_for_delete)
        else:
            answer = answer[:-1]
    return "".join(answer)


print(solution("a#bc#d"))
print(solution("abc#d##c"))
print(solution("abc##d######"))
print(solution("#######"))
print(solution(""))
