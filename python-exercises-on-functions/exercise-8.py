def AreaOfCircle(radius):
    """Define a function that accepts radius and returns 
    the area of a circle"""
    area = (22/7)* (radius**2)
    return round(area, 2)


radius = int(input("Enter the radius: "))
print("The area of the circle is " + str(AreaOfCircle(radius)))


