def repeat_me(func):

    def wrapper(*args, **kwargs):
        count = kwargs.pop('count', 1)
        for _ in range(count):
            func(*args, **kwargs)

    return wrapper


def repeat_me2(count=1):

    def function_acceptor(func):

        def wrapper(*args, **kwargs):
            for _ in range(count):
                func(*args, **kwargs)

        return wrapper

    return function_acceptor


@repeat_me
def example(text):
    print(text)


@repeat_me2(count=4)
def example1(text):
    print(text)


example('print me', count=1)
example1('print me')
