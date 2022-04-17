days = int(input())
temperature = input().split(" ")

if len(temperature) == days:
    count = dict((x, temperature.count(x)) for x in set(temperature) if temperature.count(x) >= 1)
    m = max(count.values())
    if m == 3 : m-=1
    print(m)


10
1 2 4 9 9 9 0 9 9 0