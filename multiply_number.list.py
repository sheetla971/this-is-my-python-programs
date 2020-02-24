def multiplyList(myList):
    result = 1

    for x in myList:
        result = result * x
    return result

list1 = [2, 4, 8]
list2 = [6, 12, 18]
print(multiplyList(list1))
print(multiplyList(list2))
