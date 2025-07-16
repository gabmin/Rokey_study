ca = [21, 10, 11, 15, 13]

for i in range(len(ca)):
    min = ca[i]
    min_index = i

    for j in range(i + 1, len(ca)):
        if ca[j] < min:
            min = ca[j]
            min_index = j

    temp = ca[i]
    ca[i] = ca[min_index]
    ca[min_index] = temp

print(ca)
