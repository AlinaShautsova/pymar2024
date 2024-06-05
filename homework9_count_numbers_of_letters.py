"""Module providing a function printing python version."""


def count_the_number_of_letter(line):
    """Count the number of letters without last letter."""
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
    return count_last_letter(line, answer, counter)


def count_last_letter(line, answer, counter):
    """Count last letter."""
    if counter > 1:
        answer.append(line[-1] + str(counter))
    else:
        answer.append(line[-1])
    return "".join(answer)


assert count_the_number_of_letter("cccbba") == "c3b2a"
assert count_the_number_of_letter("abeehhhhhccced") == "abe2h5c3ed"
assert count_the_number_of_letter("aaabbceedd") == "a3b2ce2d2"
assert count_the_number_of_letter("abcde") == "abcde"
assert count_the_number_of_letter("aaabbdefffff") == "a3b2def5"
