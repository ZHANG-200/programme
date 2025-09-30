def drawBox(width,height):
    
    if width < 4 or height < 4:
        print("Error: The width or height is too small")
        quit()

    print("*" * width)

    for i in range (height - 4):
        print("*"+" " * (width - 4) + "*")
    
    print("*" * width)
drawBox(20,8)

def drawBox(width, height, outline="*", fill=" "):
    if width < 4 or height < 4:
        print("Error: The width or height is too small")
        quit()
    print(outline * width)

    for i in range (height - 4):
        print(outline + fill * (width - 4) + outline)

    print(outline * width)
drawBox(24, 10, "&", ".")


def drawBox(width, height, outline="*", fill=" "):
    if width < 4 or height < 4:
        print("Error: The width or height is too small")
        quit()
    
    print(width * outline)

    for i in range (height - 4):
        print(outline + fill * (width - 1) + outline)
    
    print (width * outline)
drawBox(10, 7, "%", ",")