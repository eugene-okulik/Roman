result0 = 'результат операции: 42'
result1 = 'результат операции: 54'
result2 = 'результат работы программы: 209'
result3 = 'результат: 2'

def calc(result):
    text_res = result.split()[-1]
    num_res = int(text_res)
    print(num_res + 10)

all_result = [result0, result1, result2, result3]

for all in all_result:
    calc(all)