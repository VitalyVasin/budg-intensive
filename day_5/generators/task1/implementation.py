
def fib(n):
    """
    Функция, которая возвращает n-ое число последовательности Фибоначчи
    """
    num0, num1 = 1, 1

    for num in range(n):
        yield num0
        num_fib = num0 + num1
        num0 = num1
        num1 = num_fib

list_fib = list(fib(10))
result_fib = list_fib[-1]
print(result_fib)
