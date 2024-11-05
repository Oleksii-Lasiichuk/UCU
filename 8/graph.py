"""HW Lab week 9"""
def get_graph_from_file(filename: str) -> list[list[int]]:
    """ 
    Reads a graph from a specified file and returns a list of edges.
    The file should contain pairs of integers representing edges,
    with each edge formatted as "node1,node2" on a new line.
    For example:
        1,2
        3,4
        1,5

    Parameters:
    -----------
    filename: str
        The path to the file containing the graph edges in comma-separated format.

    Returns:
    --------
    list[list[int]]:
        A list of edges, where each edge is represented as a list of two integers.

    Example:
    --------
    >>> get_graph_from_file("data1.txt")
    [[1, 2], [3, 4], [1, 5]]
    """
    with open(filename, encoding='utf-8') as file:
        lines = file.readlines()
        output = [[int(el) for el in row.split(',')] for row in lines]
    return output

def to_edge_dict(edge_list: list[list[int]]) -> dict[int, list[int]]:
    """ 
    Converts a graph from a list of edges to a dictionary representation.
    Each node maps to a list of adjacent nodes based on the edges provided.
    The list of nodes should be sorted in ascending order.

    Parameters:
    -----------
    edge_list : list[list[int]]
        A list of edges, where each edge is represented as a list of two integers.

    Returns:
    --------
    dict[int, list[int]]:
        A dictionary with nodes as keys and lists of adjacent nodes as values.

    Example:
    --------
    >>> to_edge_dict([[1, 2], [3, 4], [1, 5], [2, 4]])
    {1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}
    """
    all_dots = set()
    output = {}
    for lst in edge_list:
        for el in lst:
            all_dots.add(el)
    all_dots = sorted(list(all_dots))
    for el in all_dots:
        output[el] = []
    for el in all_dots:
        for edge in edge_list:
            if el in edge:
                output[el].extend([char for char in edge if char != el ])
        output[el] = sorted(output[el])
    
    return output

def is_edge_in_graph(graph:  dict[int, list[int]], edge: tuple[int, int]) -> bool:
    """ 
    Checks if a given edge exists in the graph.

    Parameters:
    -----------
    graph : dict[int, list[int]]
        A dictionary representation of the graph.
    edge : tuple[int, int]
        A tuple representing the edge to check.

    Returns:
    --------
    bool:
        True if the edge exists in the graph; False otherwise.

    Example:
    --------
    >>> is_edge_in_graph({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, (3, 1))
    False
    """

    return edge[0] in graph and edge[1] in graph[edge[0]]

def add_edge(graph: dict[int, list[int]], edge: tuple[int, int]) -> dict[int, list[int]]:
    """ 
    Adds a new edge to the graph and returns the updated graph.

    Parameters:
    -----------
    graph : dict[int, list[int]]
        A dictionary representation of the graph.
    edge : tuple[int, int]
        A tuple representing the edge to add.

    Returns:
    --------
    dict[int, list[int]]:
        The updated graph with the new edge included.

    Example:
    --------
    >>> add_edge({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, (1, 4))
    {1: [2, 5, 4], 2: [1, 4], 3: [4], 4: [2, 3, 1], 5: [1]}
    """
    if not is_edge_in_graph(graph, edge):
        graph.setdefault(edge[0], []).append(edge[1])
        graph.setdefault(edge[1], []).append(edge[0])
    return graph

def del_edge(graph: dict[int, list[int]], edge: tuple[int, int]) -> dict[int, list[int]]:
    """ 
    Removes an edge from the graph and returns the updated graph.

    Parameters:
    -----------
    graph : dict[int, list[int]]
        A dictionary representation of the graph.
    edge : tuple[int, int]
        A tuple representing the edge to remove.

    Returns:
    --------
    dict[int, list[int]]:
        The updated graph with the specified edge removed.

    Example:
    --------
    >>> del_edge({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, (2, 4))
    {1: [2, 5], 2: [1], 3: [4], 4: [3], 5: [1]}
    """
    if graph.get(edge[0]) and edge[1] in graph.get(edge[0]):
        graph[edge[0]].remove(edge[1])
    if graph.get(edge[1]) and edge[0] in graph.get(edge[1]):
        graph[edge[1]].remove(edge[0])
    return graph

def add_node(graph: dict[int, list[int]], node: int) -> dict[int, list[int]]:
    """ 
    Adds a new node to the graph and returns the updated graph.

    Parameters:
    -----------
    graph : dict[int, list[int]]
        A dictionary representation of the graph.
    node : int
        The node to add to the graph.

    Returns:
    --------
    dict[int, list[int]]:
        The updated graph with the new node included.

    Example:
    --------
    >>> add_node({1: [2], 2: [1]}, 3)
    {1: [2], 2: [1], 3: []}
    """
    graph.setdefault(node, [])
    return graph

def del_node(graph: dict[int, list[int]], node: int) -> dict[int, list[int]]:
    """ 
    Deletes a node and all its incident edges from the graph.

    Parameters:
    -----------
    graph : dict[int, list[int]]
        A dictionary representation of the graph.
    node : int
        The node to delete from the graph.

    Returns:
    --------
    dict[int, list[int]]:
        The updated graph with the specified node and its edges removed.

    Example:
    --------
    >>> del_node({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, 4)
    {1: [2, 5], 2: [1], 3: [], 5: [1]}
    """
    if node in graph:
        del graph[node]
    for value in graph.values():
        if node in value:
            value.remove(node)
    return graph

def convert_to_dot(filename: str) -> None:
    """
    Reads a file of edges, converts it into a directed graph in DOT format, 
    and saves it as a file with the same name but with a .dot extension.
    
    This function allows for quick visualization and verification of 
    graph functions by exporting them in a format that can be rendered as a graph.

    Parameters:
    -----------
    filename : str
        The name of the input file containing graph edges in "node1,node2" format,
        with one edge per line.

    Returns:
    --------
    None
        Saves the directed graph in DOT format to a file with the same 
        name as the input file but with a .dot extension.
    
    Example:
    --------
    >>> import tempfile
    >>> with tempfile.NamedTemporaryFile(mode= 'w+', suffix=".txt") as temp_input:
    ...     _ = temp_input.write("1,2\\n3,4\\n1,5\\n")
    ...     _ = temp_input.seek(0)
    ...     convert_to_dot(temp_input.name)
    ...     output_file = temp_input.name.replace('.txt', '.dot')
    ...     with open(output_file, 'r') as temp_output:
    ...         print(temp_output.read())
    digraph {
    1 -> 2
    1 -> 5
    2 -> 1
    3 -> 4
    4 -> 3
    5 -> 1
    }
    """
    graph = to_edge_dict(get_graph_from_file(filename))

    new_filename = filename.replace('.txt', '.dot')
    with open(new_filename,'w', encoding='utf-8') as file:
        file.write('digraph {\n')
        for keys, edges in graph.items():
            for edge in edges:
                file.write(f'{keys} -> {edge}\n')
        file.write('}')

if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
