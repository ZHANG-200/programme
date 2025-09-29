again = "yes"
while again == "yes":
    print ("hello")
    again = input("Do you want to loop again?")

total = 0
while total < 100:
     number = int (input("Enter a number: "))
     total = total + number
print ("Hello, the total is: ",total)

x= int (input("Enter an interger (0 to quit): "))
while x !=0:
     if x > 0:
          print("That's a positive number.")
     else:
          print("That's a negative number.")
     break
