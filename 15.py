# from collections import Counter

days = int(input())
temperature = input().split(" ")

if len(temperature) <= days:
    count = dict((x, temperature.count(x)) for x in set(temperature) if temperature.count(x) > 1)
    try:
        print(max(count.values()))
    except:
        print(1)
