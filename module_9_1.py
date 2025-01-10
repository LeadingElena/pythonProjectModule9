def is_all_integers(list_numbers):
    return all(isinstance(number, int or float) for number in list_numbers)

def apply_all_func(int_list, *functions):
    if not is_all_integers(int_list):
        raise ValueError("Все элементы списка должны быть целыми числами")

    results = {}

    for func in functions:
        results[func.__name__] = func(int_list)

    return (results)

print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))

"""
Вывод на консоль:
{'max': 20, 'min': 6} 
{'len': 4, 'sum': 50, 'sorted': [6, 9, 15, 20]}
"""
