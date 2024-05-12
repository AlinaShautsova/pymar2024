print("Заменить символ “#” на символ “/” в строке 'www.my_site.com#about'")
message = "www.my_site.com#about"
print(message.replace("#", "/"))
print()

print("Напишите программу, которая добавляет ‘ing’ к словам")
message2 = "Hello world"
elements = message2.split()
arr = []
for i in elements:
    arr.append(i + 'ing')
message2 = " ".join(arr)
print(message2)
print()

print('В строке “Ivanou Ivan” поменяйте местами слова => "Ivan Ivanou"')
message3 = "Ivanou Ivan"
elements = message3.split()
message3 = " ".join(elements[::-1])
print(message3)
print()

print("Напишите программу которая удаляет пробел в начале, в конце строки")
s = " Hometask "
print(s[1:-1])
print()

print("Имена собственные всегда начинаются с заглавной буквы, за которой следуют строчные буквы. Исправьте данное имя собственное так, чтобы оно соответствовало этому утверждению.")
# "pARiS" >> "Paris"
a = "pARis"
print(a.title())
