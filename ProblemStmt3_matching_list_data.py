l1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
l2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
lt = []
for v1 in l1:
    for v2 in l2:
        if v1 == v2:
            lt.append(v1)

print(lt)

