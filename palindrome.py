number = int(input("enter any number:"))

temp = number
reverse = 0

while temp != 0:
    reverse = (reverse * 10) + (temp % 10)
    temp = temp // 10

    if number == reverse:
        print("number is palindrome")
    else:
        print("number is not palindrome")



