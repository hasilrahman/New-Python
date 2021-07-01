def checkTriangle(x, y, z):
    if x == y == z:
        print("Equilateral Triangle")

    elif x == y or y == z or z == x:
        print("Isoceles Triangle")

    else:
        print("Scalene Triangle")
