from graphviz import Digraph

# Loads a tree structure from a newick string. The returned variable ’t’ is the root node for the tree.


def edge_exists(edges, edge1, edge2):
    if not edges:
        return True
    for x in edges:
        if ((x[0] == edge1) & (x[1] == edge2)) or ((x[0] == edge2) & (x[1] == edge1)):
            return False
    return True


def draw_tree(input_array):

    g = Digraph('G', filename='hello.gv')
    edges = []
    for y in input_array:
        for x in range(len(y) - 1):
            if edge_exists(edges, y[x], y[x + 1]):
                g.edge(y[x][6:len(y[x]):], y[x+1][6:len(y[x+1]):])
                edges.append([y[x], y[x + 1]])
    # for y in input_array:
    #     for x in range(len(input_array[y]) - 1):
    #         g.edge(input_array[y][x][6:len(input_array[y][x]):], input_array[y][x+1][6: len(input_array[y][x+1]):])

    g.view()