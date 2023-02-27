# Python Program to print 2nd Largest NUmber in a list.

x = [25, 45, 10, 48, 9, 10, 98, 90, 100, 105]

fm = max(x[0], x[1])
sm = min(x[0], x[1])

for y in range(2, len(x)):
    if x[y] > fm:
        sm = fm
        fm = x[y]
    elif x[y] > sm:
        sm = x[y]
else:
    print('Second Largest Number : ', sm)

