# Python program to remove multiple elements from a list
list1 = [11, 5, 17, 18, 23, 50]

for elements in list1:
    if elements % 2 == 0:
        list1.remove(elements)

print("New list after removing all even numbers: ", list1)
