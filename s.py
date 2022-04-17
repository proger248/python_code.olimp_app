n = input()
while 1 == 1:
    try:
        z = n.index("Z")
        # print(z)
        if z < 3:
            print("Zombie")
            quit()
        n = n[:z - 2] + n[z + 1:]
        # n = n[:z-2] + "." + n[z+1:]
        print(n)
    except ValueError:
        break
print("Plant")
