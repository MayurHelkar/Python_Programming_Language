# *args

def multipleArguments(*numbers):
    print(numbers)

    print('All numbers printed seperated by Space :')
    for number in numbers:
        print(number, end = ' ')
    print()

    total = 1
    for number in numbers:
        total *= number
    return total

print("Total is ", multipleArguments(1, 2, 3, 4, 5))