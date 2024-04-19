data = [64, 25, 12, 22, 11]
for i in range(1, len(data)):
    key = data[i]
    j = i-1
    while j >= 0 and key < data[j]:
        data[j + 1] = data[j]
        j -= 1
    data[j + 1] = key
print(data)
