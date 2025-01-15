def all_variants(text):
    # Проходим по всем возможным размерам подстрок
    for size in range(len(text)):
        # Проходим по всем возможным начальным индексам подстрок заданного размера
        for i in range(len(text) - size):
            # Генерируем подстроку от индекса l до l + size + 1
            yield text[i:i + size + 1]

a = all_variants("abc")
for i in a:
    print(i)

"""
Вывод на консоль:
a
b
c
ab
bc
abc
"""