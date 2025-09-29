message = input ("Enter a message (blank to quit): ")

while message != "":
    n = int (input("How many times should it be reapted? "))
    for i in range(n):
        print(message)

    message = input("Enter a message (blank to quit): ")