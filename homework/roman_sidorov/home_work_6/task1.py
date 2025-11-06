find_var = 5

while True:
    user_var = int(input("Please enter a number: "))
    if user_var == find_var:
        print('Поздравляю! Вы угадали!')
        break
    else:
        print('попробуй снова')
