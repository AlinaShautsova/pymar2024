"""Module contains a solution to the task: files."""
import os
import json


def create_new_file(new_file):
    """Create the file if it does not exist."""
    if not os.path.exists(new_file):
        with open(new_file, "w", encoding='utf-8') as file:
            students = ('[["Kate", "Group1", [7, 8, 9]],\n'
                        '["Fedor", "Group2", [8, 7, 7]],\n'
                        '["Lena", "Group3", [9, 9, 7]],\n'
                        '["Nika", "Group3", [7, 6, 9]],\n'
                        '["Misha", "Group2", [6, 9, 7]]]')

            file.write(students)


def open_and_read(new_file):
    """The function opens and reads the file. Writes the total number of
    students."""
    with open(new_file, 'r', encoding='utf-8') as file1:
        content = file1.readlines()
    return content


def counter(content):
    """Function return counter with number of students for
         each group and average mark for each group."""
    counter_group = {}
    counter_marks = {}
    for student in content:
        _, group, marks = student
        if group not in counter_group:
            counter_group[group] = 1
            counter_marks[group] = marks
        else:
            counter_group[group] += 1
            counter_marks[group] += marks
    for key, value in counter_marks.items():
        average_value = round(sum(value) / len(value))
        counter_marks[key] = average_value
    return counter_group, counter_marks


def add_result_info(file_name, info_to_write):
    """Function adds new information in the file."""
    with open(file_name, 'a', encoding='utf-8') as file:
        file.write(info_to_write)


create_new_file("students.txt")

content_from_file = open_and_read("students.txt")
COMBINED_STRING_FROM_FILE = "".join(content_from_file).replace('\n', '')
list_of_content = json.loads(COMBINED_STRING_FROM_FILE)

amount_of_students = len(content_from_file)

amount_of_group, all_marks = counter(list_of_content)

add_result_info("students.txt", f"\nTotal number of students:"
                                f" {amount_of_students}\n")
add_result_info("students.txt", f"Number of students for"
                                f" each group{amount_of_group}. "
                                f"\nAverage marks {all_marks}")
