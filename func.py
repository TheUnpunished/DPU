def dpu(data, size):
    data = transpose(data)
    maxes = []
    indexes = []
    for k in range(len(data) - 1):
        table = []
        if k == 0:
            for i in range(len(data[k])):
                temp = []
                for j in range(len(data[k])):
                    if (i + j) < len(data[k]):
                        temp.append(data[k][j] + data[k + 1][i])
                    else:
                        temp.append(0)
                table.append(temp)
        else:
            for i in range(len(data[k])):
                temp = []
                for j in range(len(data[k])):
                    if (i + j) < len(data[k]):
                        temp.append(maxes[k-1][j] + data[k + 1][i])
                    else:
                        temp.append(0)
                table.append(temp)
        maxes_temp, indexes_temp = find_max_diag(table)
        maxes.append(maxes_temp)
        indexes.append(indexes_temp)
    rem = size[len(size) - 1]
    x_array = []
    z = 0
    for k in range(len(indexes) - 1, -1, -1):
        temp_index = size.index(rem)
        needed_index = indexes[k][temp_index][0]
        x_array.append(size[needed_index])
        z += data[k+1][needed_index]
        rem -= size[needed_index]
    x_array.append(rem)
    z += data[0][size.index(rem)]
    x_array_true = []
    for i in range(len(x_array) -1, -1, -1):
        x_array_true.append(x_array[i])
    return x_array_true, z

def transpose(array):
    result = []
    for j in range(len(array[0])):
        temp = []
        for i in range(len(array)):
            temp.append(array[i][j])
        result.append(temp)
    return result


def fill_zeros(array):
    result = []
    for i in range(len(array)):
        temp = [0]
        for j in range(len(array[i])):
            temp.append(array[i][j])
        result.append(temp)
    return result


def find_max_diag(table):
    result = []
    indexes = []
    indexes.append([0, 0])
    result.append(table[0][0])
    for i in range(1, len(table)):
        max = 0
        temp_index = []
        for j in range(i+1):
            if table[i - j][j] > max:
                max = table[i - j][j]
                temp_index = [i - j, j]
            elif table[i - j][j] == max:
                temp_index = [i - j, j]
        result.append(max)
        indexes.append(temp_index)
    return result, indexes

