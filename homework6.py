"""Module for homework6."""
print('Перевести строку в список "Robin Singh" => ["Robin”, “Singh"]')
MESSAGE1 = "Robin Singh"
print(MESSAGE1.split())
print()
print('"I love arrays they are my favorite" => ["I", "love", "arrays", "they",'
      ' "are", "my", "favorite"]')
MESSAGE2 = "I love arrays they are my favorite"
print(MESSAGE2.split())
print()
print('Дан список: [Ivan, Ivanou], и 2 строки: Minsk, Belarus')
a = ["Ivan", "Ivanou"]
b = "Minsk"
c = "Belarus"
print("Привет, {name}! Добро пожаловать в {place} "
      "{place2}".format(name=" ".join(a), place=b, place2=c))
print()
print('Дан список ["I", "love", "arrays", "they", "are", "my", "favorite"] '
      'сделайте из него строку => "I love arrays they are my favorite"')
arr = ["I", "love", "arrays", "they", "are", "my", "favorite"]
MESSAGE3 = " ".join(arr)
print(MESSAGE3)
print()
print('Создайте список из 10 элементов, вставьте на 3-ю позицию новое значение'
      ', удалите элемент из списка под индексом 6')
arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
arr1.insert(3, 'a')
print(arr1)
del arr1[6]
print(arr1)
