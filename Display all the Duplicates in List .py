# Python Program to print highest frequency of duplicate elements.

x = [10, 45, 10, 10, 45, 78, 45, 45, 90, 10]
y, z, s= [], [], []
for item in range(len(x)):
    if x[item] not in y:
        y.append(x[item])
    else:
        z.append(x[item])
        s.append(item)
else:
    print(z, s)



