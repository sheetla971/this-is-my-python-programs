def game():
    output = 'you make the wrong choice.sorry you are dead.'
    a = input("person choose door1 or door2:")
    if a == 'door1':
        print('wow! you are right and you go to the  next level')
        b = input('person choose 1 or 2:')
        if b == '1':
            print('wow! you are right and you go to the  next level')
            c = input('person choose 3 or 4:')
            if c == '3':
                print('wow! you are right and you go to the  next level')
                d = input('person choose 5 or 6:')
                if d == '5':
                    print('wow! you are right and you go to the  next level')
                    e = str(input('who is the prime minister of india:'))
                    if e == 'modi':
                        print('wow !you make the right choice.and you win the gold.')
                    else:
                        return output
                else:
                    return output
            else:
                return output
        else:
            return output
    else:
        return output
    return output


print(game())

