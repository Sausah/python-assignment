def rad_to_area(rad):
    from math import pi
    area = pi * (rad**2)
    return area
radius = float(input('Enter radius of circle: '))
print('The area of the circle is', rad_to_area(radius))
