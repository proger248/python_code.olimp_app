days = int(input())
temperature = input().split(" ")
if len(temperature) != days: quit()

res = [1]
k = 1
temp_old = temperature[0]
# print(temp_old)
for i in range(len(temperature) - 1):
    # print(i+1, ' : ',temp_old, temperature[i+1])
    if temp_old == temperature[i + 1]:
        k += 1
        # print (k)
    else:
        # print(k)
        res.append(k)
        temp_old = temperature[i + 1]
        k = 1
print(max(max(res), k))

#
#
# # print(temperature)
# temperature.sort()
# # print(temperature)
# st = set (temperature)
# # print(st)
# # print (len(st))
# # print(temperature[4])
#
# res = []
# c_old = 0
# for i in range(len(st)):
#     # print(temperature.count('2'))
#
#     # print(temperature[0])
#     c = temperature.count(temperature[0])
#     # print(c)
#     res.append(c)
#     if c > c_old :
#         if c != 1 :
#             temp = temperature[0]
#         else :
#             temp = 1
#     c_old = c
#     for d in  range(c):
#         temperature.remove(temperature[0])
#     # print(temperature)
# print(max(res))
# # print(temp)
#
# # print()
# # if len(temperature) == days:
# #     count = dict((x, temperature.count(x)) for x in set(temperature) if temperature.count(x) >= 1)
# #     print("Vadik's answer", max(count.values()))
#
# # if len(temperature) == days:
# #     count = dict((x, temperature.count(x)) for x in set(temperature) if temperature.count(x) >= 1)
# #     m = max(count.values())
# #     if m == 3 : m-=1
# #     print(m)
