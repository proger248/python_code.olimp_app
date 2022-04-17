n = input()
# print(len(n))
print(n)
old = n

while 1 == 1:
    for i in range(len(n)):
        if n[i] == ".":
            # print("Точка:",i, end=" | ")
            k1 = i - 3
            k2 = i + 4
            if k1 < 0: k1 = 0
            if k2 > len(n) : k2 = len(n)

            # print(k1, k2)
            # print(n.find("*", k1, k2), end=" | ")
            # print(n.rfind("*", k1, k2))
            if n.find("*", k1, k2) != n.rfind("*", k1, k2) and n.find("*", k1, k2) != -1 and n.rfind("*", k1, k2) != -1:
                # print("Замена", i)
                n = n[:i] + "+" + n[i + 1:]

    # print("Значение", n)
    n = n.replace("+", "*")
    if old == n : break
    # print("New Значение", n)
    print(n)
    old = n

