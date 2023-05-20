import math

num = []
x = 0

while x < 50:
    x = x +1
    num.append(x)
    for x in range(len(num)):
        if (num[x] % 2) == 0:
            flag = True
        else:
            flag = False
    # print(num)

    if flag:
        print(num[x], "is not a prime number")
        num.append(num[x])
        print(num)
    else:
        print(num[x], "is a prime number")