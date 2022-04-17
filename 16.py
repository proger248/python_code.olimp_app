n = input().split(" ")
r = int(n[0])
c = int(n[1])
s = r * c
mas = []
result = []
result2 = []

count_r = 0
while count_r < r:
    mas.append(input().split(" "))
    count_r += 1

# print(len(mas))
# print(mas)
# print(mas[1][0])

# for i in range(s):
for i in range(len(mas)):
    for k in range(c):
        # print(mas[i][k])
        value = int(mas[i][k])
        if k + 1 <= c - 1:
            result.append(mas[i][k] + mas[i][k + 1])
            result2.append(value + int(mas[i][k + 1]))
        if i + 1 <= r - 1:
            result.append(mas[i][k] + mas[i + 1][k])
            result2.append(value + int(mas[i + 1][k]))
# print(result)
# print(result2)
print(max(result2))
