def func_executor(*args):
    result = []
    for func, data in args:
        result.append(f"{func.__name__} - {func(*data)}")
    return "\n".join(result)


"""
test print
"""
def sum_numbers(num1, num2):
    return num1 + num2

def multiply_numbers(num1, num2):
    return num1 * num2

print(func_executor(
    (sum_numbers, (1, 2)),
    (multiply_numbers, (2, 4))
))