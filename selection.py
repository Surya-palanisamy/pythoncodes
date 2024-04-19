data = [6, 2, 3, 4, 1]
for i in range(len(data)):
    min_idx = i
    for j in range(i+1, len(data)):
        if data[j] < data[min_idx]:
            min_idx = j
    data[i], data[min_idx] = data[min_idx], data[i]
print(data)
