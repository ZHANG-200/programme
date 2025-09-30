def sumGeometric(a, r, n):
    if r == 1:
        return a * n
    s=a * (1 - r ** n)/ (1 - r)

    print(s) 

sumGeometric(2, 3, 10)


def get_date():
    username = input("Enter your user name:")
    age = int (input ("Enter you age:"))

    data_tuple = (username,age)

    return data_tuple

def message(username, age):
    if age <= 10:
        print("Hi", username)
    else:
        print("Hello", username)

def main():
    username, age = get_date()

    message(username,age)
main()
               