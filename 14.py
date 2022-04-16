days = int(input())
KMs = input().split(" ")
records = 0

if len(KMs) == days:
    records += 1
    # KMs.remove(KMs[0])

    for i in KMs:
        i_num = int(i)
        i_index = KMs.index(i)
        if i_num > int(KMs[i_index - 1]):
            records += 1

print(records)
