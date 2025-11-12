def finish_me(func):

    def wrapper(param):
        func(param)
        print('finished')

    return wrapper


@finish_me
def example(text):
    print(text)


example('print me')
