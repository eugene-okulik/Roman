#task1
person = ['John', 'Doe', 'New York', '+1372829383739', 'US']
name, last_name, city, phone, country = person

#task2
result1 = 'результат операции: 42'
result2 = 'результат операции: 514'
result3 = 'результат работы программы: 9'

result1 = int(result1[result1.index(':')+1: ])
result2 = int(result2[result2.index(':')+1: ])
result3 = int(result3[result3.index(':')+1: ])

print(result1+10)
print(result2+10)
print(result3+10)

#task3
students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']

print('Students', ', '.join(students)+' study these subjects:', ', '.join(subjects))