def calculator(x, y, operator):
    if operator == '+':
        result = x + y
    elif operator == '-':
        result = x - y
    elif operator == '*':
        result = x * y
    elif operator == '/':
        result = x / y
    return result

x = int(input('Введите первое число: '))
y = int(input('Введите второе число: '))
operator = input('Введите операцию (+ - * /): ')
total = calculator(x, y, operator)
print('Значение равен: ', total)





