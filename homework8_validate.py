"""Module providing a function printing python version."""
number_of_credit_card = input("Enter your card number: ")
while not number_of_credit_card.isdigit():
    print("Errors. Number of credit card must consist of digits. ")
    number_of_credit_card = input("Enter your correct card number: ")

list_with_reserved_numbers = []
for i in range(0, len(number_of_credit_card), 2):
    list_with_reserved_numbers.append(int(number_of_credit_card[i]))


list_with_reserved_numbers2 = []
for i in range(1, len(number_of_credit_card), 2):
    list_with_reserved_numbers2.append(int(number_of_credit_card[i]))

list_with_double_value = []
for number in list_with_reserved_numbers:
    list_with_double_value.append(number * 2)

for i in range(len(list_with_double_value)):
    if list_with_double_value[i] > 9:
        list_with_double_value[i] -= 9

total_sum = sum(list_with_double_value + list_with_reserved_numbers2)

if total_sum % 10 == 0:
    print("Credit card with this number exist")
elif total_sum % 10 != 0:
    print("Credit card with this number does not exist ")
