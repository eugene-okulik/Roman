import random
while True:
    salary = int(input('price:'))
    bonus = [True, False]
    random_bonus = bool(random.choice(bonus))
    if random_bonus == True:
        happy = int(salary - salary * 0.3)
        print(salary, random_bonus, happy)
    else:
        unhappy = salary
        print(salary, random_bonus, unhappy)
