import random
number1 = random.random()
number1 = number1 * 100
print(number1)

number2 = random.randint(0,1000)
number3 = random.randint(0,1000)
newrand = number2/number3
print(newrand)

number4 = random.randint(0,9)
print(number4)

number5 = random.randrange(0,100,10)
print(number5)

colour = random.choice(["red","blue","green"])
print(colour)


