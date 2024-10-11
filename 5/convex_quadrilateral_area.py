"""HW"""
import math

def lines_intersection(
    k1: int | float,
    c1: int | float,
    k2: int | float,
    c2: int | float
) -> tuple | None:
    """
    finding coordinates of the intersections 
    (angles of future rect)
    """
    if k1 == k2:
        return None
    x = -((c1 - c2) / (k1 - k2))
    y = k1 * x + c1
    y1 = k2 * x + c2
    if round(y, 2) == round(y1, 2):
        coordinate = (round(x, 2), round(y, 2))
        return coordinate
    return None

def distance(
    x1: int | float,
    y1: int | float,
    x2: int | float,
    y2: int | float
) -> float:
    """
    finding distance between two points 
    (sides of future rect)
    """
    dis = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return round(dis, 2)

def quadrangle_area(
    a: int | float,
    b: int | float,
    c: int | float,
    d: int | float,
    f1: int | float,
    f2: int | float
) -> float | None:
    """
    finding area of the rectangle
    """
    area = (4 * f1**2 * f2**2 - ((b*b + d*d - a*a - c*c)**2))/16
    if area <= 0:
        return None
    return round(math.sqrt(area), 2)

def four_lines_area(
    k1: int | float,
    c1: int | float,
    k2: int | float,
    c2: int | float,
    k3: int | float,
    c3: int | float,
    k4: int | float,
    c4: int | float
) -> (bool | float | int):
    """
    Main func
    """
    if len(locals()) != 8:
        return None

    angle_a = lines_intersection(k1, c1, k2, c2)
    angle_b = lines_intersection(k2, c2, k3, c3)
    angle_c = lines_intersection(k3, c3, k4, c4)
    angle_d = lines_intersection(k1, c1, k4, c4)

    if None in (angle_a, angle_b, angle_c, angle_d):
        return None

    a = distance(angle_a[0],angle_a[1],angle_b[0],angle_b[1])
    b = distance(angle_b[0],angle_b[1],angle_c[0],angle_c[1])
    c = distance(angle_c[0],angle_c[1],angle_d[0],angle_d[1])
    d = distance(angle_a[0],angle_a[1],angle_d[0],angle_d[1])

    f1 = distance(angle_a[0],angle_a[1],angle_c[0],angle_c[1])
    f2 = distance(angle_b[0],angle_b[1],angle_d[0],angle_d[1])
    print(a, b, c, d, f1, f2)
    answer = quadrangle_area(a, b, c, d, f1, f2)
    return answer

print(four_lines_area(0, 20, 3, -0.3, 0.1, 10, -5, 3))
print(four_lines_area(1, 10, -1, 10, 1, -10, -1, -10))
print(four_lines_area(5, -3, -0.35, 5, 0.5, -1.5, 0,2))