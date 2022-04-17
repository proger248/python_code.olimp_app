n = int(input())
old = 0
res = []
v2_list = []
v3_list = []

for i in range(n):
    v2 = (i + 1) ** 2
    v2_list.append(v2)
    v3 = (i + 1) ** 3
    v3_list.append(v3)
    # print(i+1, end=" | ")
    # print (v2, v3)

    # m = max(old, v2, v3)
    # print("max:", m)
    # res.append(m)
# print(res)

# print("v2_list", v2_list)
# print("v3_list", v3_list)

for i in range(n):
    m2 = min(v2_list)
    m3 = min(v3_list)
    res_m = min(m2, m3)
    res.append(res_m)
    try:
        v2_list.remove(res_m)
    except:
        e = 1

    try:
        v3_list.remove(res_m)
    except:
        e = 1

    # print(m2, m3)
    # print("v2_list", v2_list)
    # print("v3_list", v3_list)

# print("res", res)
print(" ".join(map(str, res)))
