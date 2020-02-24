# Python3 program to swap first and last element of a list
def swaplist(newlist):
    size = len(newlist)

    temp = newlist[1]
    newlist[1] = newlist[size - 2]
    newlist[size - 2] = temp

    return newlist
newlist = [12, 35, 9, 56, 24]


print(swaplist(newlist))

