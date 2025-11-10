import statistics

temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27, 22, 22, 23, 25, 29, 29, 31, 33, 31, 30, 32,
                30, 28, 24, 23]

warm_temperatures = list(filter(lambda x: x > 28, temperatures))
max_temperature = int(max(warm_temperatures))
min_temperature = int(min(warm_temperatures))
avg_temperature = int(statistics.mean(warm_temperatures))
print(max_temperature, min_temperature, avg_temperature)
