texts = 'Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at, dignissim vitae libero'
new_texts=texts.split()
print(new_texts)
for text in new_texts:
    if text[-1] in '.,':
        new_text = text[:-1] + 'ing' + text[-1]
    else:
        new_text = text + 'ing'
    print(new_text, end = ' ')
