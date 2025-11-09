import datetime

date = 'Jan 15, 2023 - 12:05:33'
python_date = datetime.datetime.strptime(date,'%b %d, %Y - %H:%M:%S')
python_human = python_date.strftime('%Y-%B-%d %H:%M:%S')
python_human2 = python_date.strftime('%d.%m.%Y, %H:%M')
print(python_human [5:12])
print(python_human2)
