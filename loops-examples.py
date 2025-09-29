limit = int (input("Enter an integer:"))
print ("The multiples of 3 up to and including", limit, "are: ")
for i in range (3,limit+1,3):
   print (i)

word =str(input("Enter a word:"))
print ("The word is", word, "are:")
for i in word:
   print(i)

limit = int (input("Enter an integer:"))
print ("The third value is added to ", limit , "are:")
for i in range (1,limit,2):
   print(i)