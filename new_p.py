# Количество дней
n = int(input())
# Количество конфет
a = input().split(" ")
res = []
res_str = []

if not 2 <= n <= 20: quit()
if not len(a) == n: quit()
k = 0
z = 0
for i in range(2):
    # z = i
    while k <= 1 :
        z = i
        print("i", i, "z", z)
        if z <= len(a)-1 :
            Value1 = int(a[z])
            ValueStr1 = a[z]
            while z < len(a):
                z += 2 + k
                print("k", k, "z", z)
                if z <= len(a) - 1:
                    Value1 += int(a[z])
                    ValueStr1 += a[z]
                res.append(Value1)
                res_str.append(ValueStr1)
        k += 1

print(res_str)
print(res)
print(max(res))

#
#
#
#
#
#
#
#
#
#
# # Value1 = int(a[0])
# # ValueStr1 = a[0]
# # Value2 = int(a[0])
# # ValueStr2 = a[0]
#
# # k = 1
# # while k < 100:
# for i in range(2):
#     # print("Cycle", i)
#     Value1 = int(a[i])
#     ValueStr1 = a[i]
#     while i < len(a):
#         i += 2
#         if i <= len(a) - 1:
#             Value1 += int(a[i])
#             ValueStr1 += a[i]
#
#     res.append(Value1)
#     res_str.append(ValueStr1)
#     # k += 1
#
#     # k = 1
#     # while k < 100:
# for i in range(2):
#     Value1 = int(a[i])
#     ValueStr1 = a[i]
#     while i < len(a):
#         i += 3
#         if i <= len(a) - 1:
#             Value1 += int(a[i])
#             ValueStr1 += a[i]
#
#     res.append(Value1)
#     res_str.append(ValueStr1)
# # k += 1
#
# #
# # i = 2
# # while i < len(a):
# #     # for i in range(len(a)+1):
# #     print("index", i)
# #     if i <= len(a) - 1:
# #         print("value+index", a[i])
# #         Value1 += int(a[i])
# #         ValueStr1 += a[i]
# #         if i+1 <= len(a) - 1:
# #             Value2 += int(a[i+1])
# #             ValueStr2 += a[i+1]
# #     i += 2
# # res.append(Value1)
# # res_str.append(ValueStr1)
#
#
#
# # print(ValueStr1)
# # print(Value1)
# # print(ValueStr2)
# # print(Value2)
# # res.append()
