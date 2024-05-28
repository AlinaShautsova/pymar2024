"""Module providing a function printing python version."""
presents = input("What size statues did you receive?: ")
min(presents)
max(presents)
empty_list = []
for i in range(int(min(presents)), int(max(presents)) + 1):
    empty_list.append(i)
answer = len(empty_list) - len(presents)
print(f"Answer: {answer}")
