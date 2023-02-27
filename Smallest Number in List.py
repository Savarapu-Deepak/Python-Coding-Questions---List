# Python Program to print Smallest Number in List

x = [25, 1, 0, 85, 89, 14, -56, -10]
min_num = x[0]
for y in x:
    if y < min_num:
        min_num = y
else:
    print(min_num)