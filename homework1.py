# "Строки и индексация строк"
#1. В переменную example запишите любую строку.
#2. Выведите на экран(в консоль) первый символ этой строки.
#3. Выведите на экран(в консоль) последний символ этой строки (используя отрицательный индекс).
#4. Выведите на экран(в консоль) вторую половину этой строки (С нечётным количеством символов: 'Urban' -> 'ban').
#5. Выведите на экран(в консоль) это слово наоборот.
#6. Выведите на экран(в консоль) каждый второй символ этой строки. (Пример: 'Топинамбур'->'оиабр')

example = "Высокотехнологичный"
print(len(example))
print(example[0])
print(example[-1])
print(example[-10:])
print(example[::-1])
print(example[::])
print(example[::2])
print(example[1::2])

