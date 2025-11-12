first = int(input('first number='))
second = int(input('second number='))


def operation_dec(func):

    def wrapper(first, second):
        if first - second == 0:
            operation = '+'
        elif first - second > 0:
            operation = '-'
        elif first - second < 0:
            operation = '/'
        elif first < 0 or second < 0:
            operation = '*'

        return func(first, second, operation)

    return wrapper


@operation_dec
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '/':
        return first / second
    elif operation == '*':
        return first * second
    else:
        return 'no operation'


calc(first, second)
