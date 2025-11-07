import random

while True:
    salary = int(input('price: '))
    bonus = [True, False]
    random_bonus = bool(random.choice(bonus))
    if random_bonus is True:
        final_salary = int(salary - salary * 0.3)
    else:
        final_salary = salary
    print(salary, random_bonus, final_salary)
