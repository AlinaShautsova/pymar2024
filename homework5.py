"""Module providing a function printing python version."""
print("Заменить символ “#” на символ “/” в строке 'www.my_site.com#about'")
MESSAGE = "www.my_site.com#about"
print(MESSAGE.replace("#", "/"))
print()

print("Напишите программу, которая добавляет ‘ing’ к словам")
MESSAGE2 = "Hello world"
elements = MESSAGE2.split()
arr = []
for i in elements:
    arr.append(i + 'ing')
MESSAGE2 = " ".join(arr)
print(MESSAGE2)
print()

print('В строке “Ivanou Ivan” поменяйте местами слова => "Ivan Ivanou"')
MESSAGE3 = "Ivanou Ivan"
elements = MESSAGE3.split()
MESSAGE3 = " ".join(elements[::-1])
print(MESSAGE3)
print()

print("Напишите программу которая удаляет пробел в начале, в конце строки")
S = " Hometask "
print(S[1:-1])
print()

print("Имена собственные всегда начинаются с заглавной буквы, "
      "за которой следуют строчные буквы. Исправьте данное имя "
      "собственное так, чтобы оно соответствовало этому утверждению.")
# "pARiS" >> "Paris"
A = "pARis"
print(A.title())
