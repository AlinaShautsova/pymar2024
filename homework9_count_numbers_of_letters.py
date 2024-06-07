"""Module providing a function printing python version."""


def count_the_number_of_letters(line):
    """Count the number of letters."""
    counter = 1
    answer = []
    for i in range(1, len(line)):
        if line[i] == line[i - 1]:
            counter += 1
        else:
            if counter > 1:
                answer.append(line[i - 1] + str(counter))
            else:
                answer.append(line[i - 1])
            counter = 1

    if counter > 1:
        answer.append(line[-1] + str(counter))
    else:
        answer.append(line[-1])
    return "".join(answer)


assert count_the_number_of_letters("cccbba") == "c3b2a", \
    "Function with input value 'cccbba', not equal 'c3b2a'."
assert count_the_number_of_letters("abeehhhhhccced") == "abe2h5c3ed", \
    "Function with input value 'abeehhhhhccced', not equal 'abe2h5c3ed'."
assert count_the_number_of_letters("aaabbceedd") == "a3b2ce2d2", \
    "Function with input value 'aaabbceedd', not equal 'a3b2ce2d2'."
assert count_the_number_of_letters("abcde") == "abcde", \
    "Function with input value 'abcde', not equal 'abcde'."
assert count_the_number_of_letters("aaabbdefffff") == "a3b2def5",  \
    "Function with input value 'aaabbdefffff', not equal 'a3b2def5'."
