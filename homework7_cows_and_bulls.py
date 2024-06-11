"""Module providing a function printing python version."""
import random
from typing import List

print("Game 'Bulls and Cows'!")

list_with_random_numbers: List[int] = []
while len(list_with_random_numbers) != 4:
    random_element = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
    if random_element not in list_with_random_numbers:
        list_with_random_numbers.append(random_element)
print(list_with_random_numbers)

common_cows: List[int] = []
common_bulls: List[int] = []
while True:
    common_cows.clear()
    common_bulls.clear()
    str_from_player = input("Enter you prediction: ")
    if (len(str_from_player) != len(set(str_from_player)) or
            len(str_from_player) != 4):
        print("Numbers must be unique and contains 4 integers")
        continue

    list_from_player = []
    for char in str_from_player:
        list_from_player.append(int(char))

    for i in range(4):
        if list_from_player[i] == list_with_random_numbers[i]:
            common_bulls.append(list_from_player[i])
    print(f"{len(common_bulls)} Bulls")

    for item in list_from_player:
        if item in list_with_random_numbers:
            common_cows.append(item)
    print(f"{len(common_cows) - len(common_bulls)} Cows")

    if len(common_bulls) == 4:
        print("Congratulations! You are winner!")
        break
