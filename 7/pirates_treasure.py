"""Capitan"""
def define_direction(previous_direction, azimuth):
    """
    Calculate the new path direction based on the current direction
    and the pirate's biased azimuth. The azimuth is given in degrees
    and can be any non-negative multiple of 90. The directions are 
    represented as 'N' for North, 'E' for East, 'S' for South, and 'W' 
    for West.

    Args:
    previous_direction (str): The current direction ('N', 'E', 'S', 'W').
    azimuth (int): The azimuth in degrees (non-negative multiple of 90).

    Returns:
    str: The new direction as a single character string.

    For example:
    - If the current direction is North ('N') and the azimuth is 90 degrees,
      the new direction will be East ('E').
    - If the current direction is South ('S') and the azimuth is 90 degrees,
      the new direction will be West ('W').

    >>> define_direction('N', 0)
    'N'
    >>> define_direction('N', 90)
    'E'
    >>> define_direction('N', 180)
    'S'
    >>> define_direction('N', 270)
    'W'
    >>> define_direction('E', 90)
    'S'
    >>> define_direction('W', 270)
    'S'
    """
    directions = ["N", "E", "S", "W"]
    new_index = int(directions.index(previous_direction) + (azimuth / 90)) % 4
    return directions[new_index]

def read_map(file_name):
    """
    Reads a map from the specified file and interprets the directions
    and steps for navigation. The map file contains information about
    the starting coordinates and the steps to be taken in a specified
    direction. The initial direction is assumed to be North.

    The map file should be structured in such a way that it lists the
    starting coordinates (x, y) followed by directions (N, E, S, W)
    and the corresponding number of steps to take in each direction.

    Note: The file may contain empty lines, which should be ignored.

    Args:
    file_name (str): The pathname of the file containing the map data.

    Returns:
    tuple: A tuple containing two elements:
        - The first element is a tuple (x, y) representing the starting
          coordinates.
        - The second element is a list of tuples, where each tuple contains:
            - A direction (str): 'N' for North, 'E' for East, 'S' for South,
              or 'W' for West.
            - The number of steps (int) to take in that direction.

    >>> read_map("treasure_3.txt")
    ((0, 11), \
[('W', 5), ('W', 6), ('S', 7), ('E', 3), ('E', 4), \
('N', 5), ('E', 2), ('S', 2), ('E', 2), ('N', 4)])
    """
    with open(file_name, encoding="utf-8") as file:
        all_lines = file.read().splitlines()
        lines = []
        direction = "N"
        for i, line in enumerate(all_lines):
            if line != "" and i != 0:
                line = line.split()
                new_direction = define_direction(direction, int(line[0]))
                lines.append((new_direction, int(line[1])))
                direction = new_direction
        first_coordinate = all_lines[0].split()
    return ((int(first_coordinate[0]), int(first_coordinate[1])), lines)


def find_path(start: tuple, treasure_directions: list) -> list:
    """
    Calculates the path of coordinates based on the given start position
    and a series of directional steps. The start position is provided as
    a tuple of coordinates (x, y).

    The function interprets movement based on the following directional
    rules, with steps determining how far to move in a given direction:
    - 'W' (West): decreases the y-coordinate (moves left).
    - 'E' (East): increases the y-coordinate (moves right).
    - 'N' (North): decreases the x-coordinate (moves up).
    - 'S' (South): increases the x-coordinate (moves down).

    Args:
    start (tuple): A tuple representing the starting coordinates (x, y).
    treasure_directions (list of tuple): A list of tuples where each tuple
                                         contains:
                                         - A direction ('N', 'E', 'W', 'S')
                                         - An integer representing the number
                                           of steps to take in that direction.

    Returns:
    list of tuple: A list of coordinates (x, y) representing the path taken 
                   from the start position, including all intermediate steps.

    >>> start = (0, 0)
    >>> path = [('E', 3), ('S', 3), ('W', 3), ('N', 3)]
    >>> find_path(start, path)
    [(0, 0), \
(0, 1), (0, 2), (0, 3), \
(1, 3), (2, 3), (3, 3), \
(3, 2), (3, 1), (3, 0), \
(2, 0), (1, 0), (0, 0)\
]
    """
    path = [start]
    last_x, last_y = start[0], start[1]
    for action in treasure_directions:
        match action:
            case ('E', y):
                for _ in range(y):
                    path.append((last_x, last_y + 1))
                    last_y += 1
            case ('W', y):
                for _ in range(y):
                    path.append((last_x, last_y - 1))
                    last_y -= 1
            case ('N', y):
                for _ in range(y):
                    path.append((last_x - 1, last_y))
                    last_x -= 1
            case ('S', y):
                for _ in range(y):
                    path.append((last_x + 1, last_y))
                    last_x += 1
    return path

def find_treasure(path1, path2):
    """
    Determines the location of the treasure based on the intersection of
    two paths. The function identifies the point of intersection and
    calculates the treasure's location based on the following conditions:

    - If the paths intersect at exactly one point, that point is the
      treasure's location.
    - If the paths intersect at exactly two points, the treasure is located
      at the midpoint between these two points. If the coordinates of the
      midpoint are fractional, they are rounded down to the nearest integer.
    - If the paths intersect at more than two points, it is impossible
      to determine the treasure's exact location, and the function
      returns `None`.

    Args:
    path1 (list of tuple): The first path, represented as
                           a list of coordinates (x, y).
    path2 (list of tuple): The second path, represented as
                           a list of coordinates (x, y).

    Returns:
    tuple or None: The coordinates (x, y) of the treasure if it
    can be determined, or `None`  if the treasure's location
    cannot be identified.

    >>> path1 = [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (2, 1), (2, 0), (1, 0), (0, 0)]
    >>> path2 = [(2, 4), (2, 3), (2, 2), (3, 2), (4, 2), (4, 3), (4, 4), (3, 4), (2, 4)]
    >>> path3 = [(1, 4), (1, 3), (1, 2), (2, 2), (3, 2), (3, 3), (3, 4), (2, 4), (1, 4)]
    >>> find_treasure(path1, path2)
    (2, 2)
    >>> find_treasure(path1, path3)
    (1, 2)
    >>> find_treasure(path2, path3)
    """
    intersections = [el for el in path1 if el in path2]
    if len(intersections) > 2:
        return None
    if len(intersections) == 1:
        return intersections[0]
    if len(intersections) == 2:
        x = int((intersections[0][0] + intersections[1][0])/2)
        y = int((intersections[0][1] + intersections[1][1])/2)
        return (x, y)

def find_size(path):
    """
    Calculates the size of the map based on the given path. The size of the map
    is determined by the minimal number of points needed vertically and
    horizontally to encompass the entire path. The height is the difference
    between the maximum and minimum x-coordinates, and the width is the
    difference between the maximum and minimum y-coordinates.

    Args:
    path (list of tuple): A list of coordinates (x, y) representing the path.

    Returns:
    tuple: A tuple (height, width) where:
        - height is the number of points needed vertically.
        - width is the number of points needed horizontally.

    >>> path = [(2, 4), (2, 3), (2, 2), (3, 2), (4, 2), (4, 3), (4, 4), (3, 4), (2, 4)]
    >>> find_size(path)
    (3, 3)
    """
    all_x, all_y = sorted([x for x, _ in path]), sorted([y for _, y in path])
    return (all_x[-1] - all_x[0] + 1, all_y[-1] - all_y[0] + 1)

def shift_path(path):
    """
    Shifts the given path to ensure that all coordinates are non-negative
    and the smallest coordinate is positioned at (0, 0).

    The function returns a tuple, where the first element is a tuple
    containing the minimum y and x values before the shift, and the second
    element is the list of shifted coordinates.

    Args:
    path (list of tuple): A list of tuples where each tuple represents a
                          coordinate (x, y) along the path.

    Returns:
    tuple: A tuple where:
        - The first element is a tuple representing the minimum
          y-coordinate and x-coordinate found in the path.
        - The second element is a list of tuples representing the shifted path,
          where all coordinates are non-negative.

    >>> path = [(2, 4), (2, 3), (2, 2), (3, 2), (4, 2), (4, 3), (4, 4), (3, 4), (2, 4)]
    >>> shift_path(path)
    ((2, 2), [(0, 2), (0, 1), (0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (1, 2), (0, 2)])
    """
    all_x, all_y = sorted([x for x, _ in path]), sorted([y for _, y in path])
    new_path = []
    start_point = (all_x[0], all_y[0])
    for x, y in path:
        if all_x[0] < 0:
            x += abs(start_point[0])
        if all_y[0] < 0:
            y += abs(start_point[1])
        if all_x[0] > 0:
            x -= abs(start_point[0])
        if all_y[0] > 0:
            y -= abs(start_point[1])
        new_path.append((x, y))
    return (start_point, new_path)


def decode_map(file_name1, file_name2, map_file_name):
    """
    Draws a map that visualizes two paths and the treasure (if it exists)
    based on the paths provided in two input files. The map is written
    to the specified output file.

    - The paths are marked with `.`.
    - The start of the first path is marked with `1`.
    - The start of the second path is marked with `2`.
    - If the start of the first and second path coincides, it is
      marked with `3`.
    - If the treasure is found (i.e., the paths intersect at a specific point),
      it is marked with `x`. The treasure marker `x` overwrites the start
      markers '1' and '2' if they coincide with the treasure's location.

    Args:
    file_name1 (str): The name of the file containing the first path.
    file_name2 (str): The name of the file containing the second path.
    map_file_name (str): The name of the output file where the map will be drawn.

    Returns:
    None: The map is written directly to the output file.

    >>> decode_map('treasure_1.txt', 'treasure_2.txt', 'output.txt')
    >>> with open('output.txt', 'r', encoding='utf-8') as file:
    ...    print(file.read())
    1..  
    . .  
    ..x.2
      . .
      ...
    """
    # Read and parse the paths from both files
    start1, directions1 = read_map(file_name1)
    start2, directions2 = read_map(file_name2)
    
    # Find the path coordinates for both paths
    path1 = find_path(start1, directions1)
    path2 = find_path(start2, directions2)
    
    # Determine the treasure location if any
    treasure = find_treasure(path1, path2)
    
    # Determine the map size to ensure paths fit within the output grid
    size1 = find_size(path1)
    size2 = find_size(path2)
    height, width = max(size1[0], size2[0]), max(size1[1], size2[1])
    
    # Adjust both paths to fit within a non-negative coordinate system
    start1_shifted, shifted_path1 = shift_path(path1)
    start2_shifted, shifted_path2 = shift_path(path2)
    
    # Adjust the treasure's coordinates if it's present
    if treasure:
        treasure = (treasure[0] - min(start1_shifted[0], start2_shifted[0]),
                    treasure[1] - min(start1_shifted[1], start2_shifted[1]))
    
    # Create an empty grid based on the calculated map size
    map_grid = [[' ' for _ in range(width)] for _ in range(height)]
    
    # Mark paths on the map
    for (x, y) in shifted_path1:
        map_grid[x][y] = '.'
    for (x, y) in shifted_path2:
        map_grid[x][y] = '.'
    
    # Mark the starting points
    start1_pos = (start1_shifted[0], start1_shifted[1])
    start2_pos = (start2_shifted[0], start2_shifted[1])
    
    if start1_pos == start2_pos:
        map_grid[start1_pos[0]][start1_pos[1]] = '3'  # Overlapping start
    else:
        map_grid[start1_pos[0]][start1_pos[1]] = '1'
        map_grid[start2_pos[0]][start2_pos[1]] = '2'
    
    # Mark the treasure if it's found
    if treasure:
        map_grid[treasure[0]][treasure[1]] = 'x'
    
    # Write the grid to the output file
    with open(map_file_name, 'w', encoding='utf-8') as file:
        for row in map_grid:
            file.write(''.join(row) + '\n')

if __name__ == '__main__':
    import doctest
    doctest.testmod()
