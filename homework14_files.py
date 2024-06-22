"""Module contains a solution to the task: files."""
import json
import sys
try:
    with open('students.txt', 'r', encoding='utf-8') as file:
        content = file.readlines()
        amount_of_students = len(content)
        print(f"Total number of students: {amount_of_students}")
except FileNotFoundError:
    print("File not found. Exiting program.")
    sys.exit(1)


def counter():
    """Function return dictionary counter with number of students for
     each group and average grade for each group."""
    dictionary_counter = {}
    for string_json in content:
        dictionary = json.loads(string_json)
        if dictionary["group"] not in dictionary_counter:
            dictionary_counter[dictionary["group"]] = 1
            dictionary_counter[dictionary["group"] + "_mark"] = \
                dictionary["marks"]
            dictionary_counter[dictionary["group"] + "_average_rating"] = \
                (round(sum(dictionary_counter[dictionary["group"] + "_mark"]) /
                       len(dictionary_counter[dictionary["group"] + "_mark"])))
        else:
            dictionary_counter[dictionary["group"]] += 1
            dictionary_counter[dictionary["group"] + "_mark"] += (
                dictionary)["marks"]
            dictionary_counter[dictionary["group"] + "_average_rating"] = (
                round(sum(dictionary_counter[dictionary["group"] + "_mark"]) /
                      len(dictionary_counter[dictionary["group"] + "_mark"])))
    print(dictionary_counter)
    return dictionary_counter


with open('students.txt', 'a', encoding='utf-8') as file:
    file.write(f"\nTotal number of students: {amount_of_students}\n")
    file.write(str(counter()))
