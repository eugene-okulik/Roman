def fibonacci(limit = 1000000):
    argument1, argument2 = 0, 1
    count = 0
    while count < limit:
        yield  argument1
        argument1, argument2 = argument2, argument1 + argument2
        count += 1


count = 1
for number in fibonacci(1000000):
        if count == 5:
            print(f"5-е число:{number}")
        elif count == 200:
            print(f"200-е число:{number}")
        elif count == 1000:
            print(f"1000-е число:{number}")
        elif count == 1000000:
            print(f"100000-е число:{number}")
            break
        count += 1
