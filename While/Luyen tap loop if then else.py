__author__ = 'Admin'
while True:
    number = int(input("Enter a odd number"))
    if number % 2 == 0:
        print("your number is even number")
    while 0 != number % 2:
        for i in range(1, number + 1):
            for j in range(1, i + 1):
                print(j, end="")
            print("")
        else:
            break