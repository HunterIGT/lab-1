print('hello world')

'''
doc
so mush strings
'''

flag = True
while flag:

    value_1 = int (input("val1= "))
    value_2 = int (input("val2= "))

    command = input("input operator")

    if command == '+':
        print(value_1 + value_2)
    elif command == '-':
        print(value_1 - value_2)
    elif command == '*':
        print(value_1 * value_2)
    elif command == '/':
        print(value_1 // value_2)
    else:
        print("wrong command")

    for i in range(3):
        command = input("Countine? Y/N\n")
        if command == 'Y':
            break
        elif command == 'N':
            flag = False
            break
        else:
            print("wrong command")
        if i == 2:
            print("too many errors!")
            flag = False
            break



    #doc one string
