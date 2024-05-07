def is_safe(vertex, color, graph, color_array):
    """
    Check if it's safe to assign a color to a vertex.
    
    Parameters:
        vertex (int): The vertex to check.
        color (int): The color to be assigned to the vertex.
        graph (dict): The graph represented as an adjacency list.
        color_array (list): An array storing colors assigned to vertices.
        
    Returns:
        bool: True if it's safe to assign the color to the vertex, False otherwise.
    """
    for neighbor in graph[vertex]:
        # Check if any neighbor has the same color as the one we want to assign
        if color_array[neighbor] == color:
            return False
    return True

def graph_valid_color(graph, num_colors, vertex, color_array):
    """
    Recursively explores possible colorings of the graph until a valid solution is found.
    
    Parameters:
        graph (dict): The graph represented as an adjacency list.
        num_colors (int): The number of available colors.
        vertex (int): The current vertex being colored.
        color_array (list): An array storing colors assigned to vertices.
        
    Returns:
        bool: True if a valid coloring is found, False otherwise.
    """
    if vertex == len(graph):
        # Base case: If all vertices are colored, return True
        return True
    
    for color in range(1, num_colors + 1):
        # Try assigning colors to the current vertex
        if is_safe(vertex, color, graph, color_array):
            color_array[vertex] = color
            # Recursively call graph_valid_color for the next vertex
            if graph_valid_color(graph, num_colors, vertex + 1, color_array):
                return True  # If a solution is found, return True
            color_array[vertex] = 0  # Backtrack if no color works for the current vertex
    
    return False

def graph_coloring(graph, num_colors):
    """
    Assigns colors to vertices of the graph using a backtracking algorithm.
    
    Parameters:
        graph (dict): The graph represented as an adjacency list.
        num_colors (int): The number of available colors.
        
    Returns:
        bool: True if a valid coloring is found, False otherwise.
    """
    color_names = ["Red", "Green", "Blue"]  # Color names corresponding to color numbers
    color_array = [0] * len(graph)  # Array to store colors assigned to vertices
    
    if not graph_valid_color(graph, num_colors, 0, color_array):
        # If no solution exists, print a message and return False
        print("No solution exists")
        return False
    
    # If a solution exists, print the coloring of vertices
    print("Solution exists and the coloring is:")
    for i, color in enumerate(color_array):
        print(f"Vertex {i} --> Color {color_names[color - 1]}")
    
    return True

if __name__ == "__main__":
    # Define the graph as an adjacency list
    graph = {
        0: [1, 2],
        1: [0, 2],
        2: [0, 1, 3, 4, 5],
        3: [1, 2, 4],
        4: [2, 3, 5],
        5: [2, 4],
        6: [2, 5]
    }
    num_colors = 3  # Number of available colors
    graph_coloring(graph, num_colors)
