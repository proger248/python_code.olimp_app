from math import fabs

n = int(input())

if 2 <= n <= 8:
    r = n + (n - 1)  # Количество строк
    s = n * 4 - 3  # Количество знаков
    # print(f"r = {r}")
    # print(f"s = {s}")

    for i in range(r):
        k = int(fabs(n - (i + 1)))
        stars_col = n + (n - 1) - k

        DOTs1 = "." * k
        DOTs2 = "." * (k - 1)
        center = "*." * (stars_col - 1) + "*"
        mas = DOTs1 + center + DOTs1

        print(mas)
