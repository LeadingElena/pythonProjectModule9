def is_prime(func):
    def wrapper(*args):
        result_func = func(*args)
        # Проверяем, является ли число меньше 2
        if result_func < 2:
            print('Составное')  # Числа меньше 2 не являются простыми
            return result_func
        for i in range(2, int(result_func ** 0.5) + 1):
            # Если n делится на i, то оно составное
            if result_func % i == 0:
                print('Составное')
                return result_func
        print('Простое')
        return result_func  # Если не нашли делителей, число простое
    return wrapper

@ is_prime
def sum_three(a, b, c):
    return a + b + c

result = sum_three(2, 3, 6)
print(result)

"""
Результат консоли:
Простое
11
"""