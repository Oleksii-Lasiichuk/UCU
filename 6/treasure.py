"""pirates"""
def find_path(treasure_map: list) -> list:
    """
    Finds the path in coordinates according to treasure_map
    assuming that start is in (0, 0).
    If we go left by 1 from the start, the coordinate is (0, -1).
    If right – (0, 1).
    If we go up by 1 from the start, the coordinate is (-1, 0).
    If down – (1, 0).
    Return the list of coordinates.

    >>> find_path([('U', 2), ('R', 2), ('D', 2), ('R', 2), ('U', 4), ('L', 11), \
('D', 7), ('R', 7), ('U', 3)])
    [(0, 0), (-1, 0), (-2, 0), (-2, 1), (-2, 2), \
(-1, 2), (0, 2), (0, 3), (0, 4), (-1, 4), (-2, 4), \
(-3, 4), (-4, 4), (-4, 3), (-4, 2), (-4, 1), (-4, 0), \
(-4, -1), (-4, -2), (-4, -3), (-4, -4), (-4, -5), \
(-4, -6), (-4, -7), (-3, -7), (-2, -7), (-1, -7), \
(0, -7), (1, -7), (2, -7), (3, -7), (3, -6), \
(3, -5), (3, -4), (3, -3), (3, -2), (3, -1), \
(3, 0), (2, 0), (1, 0), (0, 0)]

    """
    path = [(0, 0)]
    last_x = 0
    last_y = 0
    coordinates = []
    x, y = 0, 0
    for action in treasure_map:
        for _ in range(1, action[1]+1):
            if action[0] == "U":
                x = last_x - 1
                coordinates = (x, last_y)
                path.append(coordinates)
                last_x -= 1
            elif action[0] == "R":
                y = last_y + 1
                coordinates = (last_x, y)
                path.append(coordinates)
                last_y += 1
            elif action[0] == "D":
                x = last_x + 1
                coordinates = (x, last_y)
                path.append(coordinates)
                last_x += 1

            elif action[0] == "L":
                y = last_y - 1
                coordinates = (last_x, y)
                path.append(coordinates)
                last_y -= 1
    return path

def find_positive_path(path: list) -> list:
    '''Find the path with nonnegative coordinates by shifting
    the path horizontally and vertically by minimal steps.
    >>> treasure_map = [('U', 2), ('R', 2), ('D', 2), ('R', 2), ('U', 4), ('L', 11), \
('D', 7), ('R', 7), ('U', 3)]
    >>> path = find_path(treasure_map)
    >>> find_positive_path(path)
    [(4, 7), (3, 7), (2, 7), (2, 8), (2, 9), (3, 9), \
(4, 9), (4, 10), (4, 11), (3, 11), (2, 11), (1, 11), \
(0, 11), (0, 10), (0, 9), (0, 8), (0, 7), (0, 6), (0, 5), \
(0, 4), (0, 3), (0, 2), (0, 1), (0, 0), (1, 0), (2, 0), \
(3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (7, 1), (7, 2), \
(7, 3), (7, 4), (7, 5), (7, 6), (7, 7), (6, 7), (5, 7), (4, 7)]
    '''
    min_x, min_y = 1, 1
    for coordinate in path:
        if coordinate[0] < min_x:
            min_x = coordinate[0]
        if coordinate[1] < min_y:
            min_y = coordinate[1]

    x, y = 0, 0
    positive_path = []
    for coordinate in path:
        if min_x <= 0:
            x = coordinate[0] + abs(min_x)
        if min_y <= 0:
            y = coordinate[1] + abs(min_y)
        coordinates = (x, y)
        positive_path.append(coordinates)
    return positive_path


def find_size(path: list) -> tuple:
    '''Finds the size of the map: minimal number of points vertically
    and horizontally needed to build the path. Return tuple where the
    first coordinate is the height of the map and the second is the length.
    >>> treasure_map = [('U', 2), ('R', 2), ('D', 2), ('R', 2), \
('U', 4), ('L', 11), ('D', 7), ('R', 7), ('U', 3)]
    >>> find_size(find_positive_path(find_path(treasure_map)))
    (8, 12)
    '''
    min_x, min_y = 1, 1
    for coordinate in path:
        if coordinate[0] < min_x:
            min_x = coordinate[0]
        if coordinate[1] < min_y:
            min_y = coordinate[1]
    max_x, max_y = 1, 1
    for coordinate in path:
        if coordinate[0] > max_x:
            max_x = coordinate[0]
        if coordinate[1] > max_y:
            max_y = coordinate[1]

    size = (max_x - min_x + 1, max_y - min_y + 1)
    return size

def view_map(path: list) -> str:
    '''
    From path creates the map. Returns string representation of the map.
    If the coordinate is on the path, put the symbol 'x'. 
    Otherwise use '.'.

    >>> treasure_map = [('U', 2), ('R', 2), ('D', 2), ('R', 2), \
('U', 4), ('L', 11), ('D', 7), ('R', 7), ('U', 3)]
    >>> path = find_path(treasure_map)
    >>> view_map(path)
    'xxxxxxxxxxxx\\n\
x..........x\\n\
x......xxx.x\\n\
x......x.x.x\\n\
x......x.xxx\\n\
x......x....\\n\
x......x....\\n\
xxxxxxxx....'
    '''
    positive_path = find_positive_path(path)
    size = find_size(positive_path)
    map_of_treasures = []

    for _ in range(size[0]):
        list_of_dots = ["."] * size[1]
        map_of_treasures.append(list_of_dots)

    for el in positive_path:
        x = el[0]
        y = el[1]
        map_of_treasures[x][y] = "x"

    row = ''
    full_map = ''
    for i, el in enumerate(map_of_treasures):
        row = "".join(el)
        if i == size[0]-1:
            full_map += row
        else:
            full_map += row + '\n'
    return full_map



def find_vertices(treasure_map: list) -> list:
    '''Find the vertices of polygon that created on our map.

    >>> treasure_map = [('U', 2), ('R', 2), ('D', 2), ('R', 2), \
('U', 4), ('L', 11), ('D', 7), ('R', 7), ('U', 3)]
    >>> find_vertices(treasure_map)
    [(-2, 0), (-2, 2), (0, 2), (0, 4), (-4, 4), (-4, -7), (3, -7), (3, 0)]
    >>> treasure_map = [('U', 2), ('R', 2), ('R', 2), ('D', 2), ('L', 4)]
    >>> find_vertices(treasure_map)
    [(0, 0), (-2, 0), (-2, 4), (0, 4)]

    '''
    path = find_path(treasure_map)
    vertices = []
    if path[0][0] != path[1][0] and path[0][1] != path[-2][1] or \
        path[0][1] != path[1][1] and path[0][0] != path[-2][0]:
        vertices.append(path[0])
    for i, coordinate in enumerate(path):
        if coordinate != (0, 0):
            if path[i-1][0] != path[i+1][0] and path[i-1][1] != path[i+1][1]:
                vertices.append(coordinate)
    return vertices

def calculate_polygon_area(vertices: list) -> int:
    '''
    Calculate the polygon area using the list of vertices of the
    polygon.
    #Area = 0.5 * |(x_1 * y_2 - x_2 * y_1) + (x_2 * y_3 - x_3 * y_2) + ...+
    # + (x_n * y_1 - x_1 * y_n)|
    >>> vertices = find_vertices([('U', 2), ('R', 2), ('D', 2), ('R', 2), \
('U', 4), ('L', 11), ('D', 7), ('R', 7), ('U', 3)])
    >>> calculate_polygon_area(vertices)
    61
    '''
    area = 0
    all_x = []
    for el in vertices:
        all_x.append(el[0])
    all_y = []
    for el in vertices:
        all_y.append(el[1])
    lenght = len(all_y)
    for i in range(lenght):
        if i != lenght-1:
            area += all_x[i] * all_y[i+1] - all_x[i+1] * all_y[i]
        else:
            area += all_x[i] * all_y[0] - all_x[0] * all_y[i]
    area = abs(area) * 0.5
    return int(area)

def find_volume_treasure(area: int, length: int) -> int:
    '''
    Find the number of interior points. Each point is one treasure.
    >>> treasure_map = [('U', 2), ('R', 2), ('D', 2), ('R', 2), ('U', 4), \
('L', 11), ('D', 7), ('R', 7), ('U', 3)]
    >>> vertices = find_vertices(treasure_map)
    >>> area = calculate_polygon_area(vertices)
    >>> length = len(find_path(treasure_map))-1
    >>> find_volume_treasure(area, length)
    42
    '''
    treasures = abs(length / 2 - 1 - area)
    return int(treasures)

if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
