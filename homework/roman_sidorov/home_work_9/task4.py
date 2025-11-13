PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

PRICE_LIST_IN_LIST = {
    line.split()[0]: int(line.split()[1].rstrip('р'))
    for line in PRICE_LIST.splitlines()
}

print(PRICE_LIST_IN_LIST)
