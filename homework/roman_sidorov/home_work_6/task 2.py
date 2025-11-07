words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}

for word in words.items():
    key, value = word
    print(key * value)
