count = 0
def increment():
    global count 
    count += 1

def main():
    print (f"Initial count: {count}")
    increment()
    print(F"Count after increment: {count}")

if __name__ == "__main__":
    main()