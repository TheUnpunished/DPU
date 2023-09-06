import func
from ast import literal_eval

data = []
file_data = []
with open('data3.csv') as numbers:
    file_data = numbers.read().splitlines()

size = literal_eval(file_data[len(file_data) - 1])
print()
for i in range(len(file_data) - 1):
    data.append(literal_eval(file_data[i]))
result, z = func.dpu(data, size)
print("F =", z)
print("Распределение:", result)