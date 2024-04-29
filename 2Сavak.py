def find_x(list1):
    i = 0
    for a in list1:
        if a == 6:
            return i
        i += 1

print(find_x([4,4,3,4,22,6]))