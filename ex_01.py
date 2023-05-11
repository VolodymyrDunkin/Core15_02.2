lst = [1, 2, 5, 7, 10, 3, 9, 0]
print(max(lst))

k = 0

for i in lst:
    if k < i:
        k = i

print(k)