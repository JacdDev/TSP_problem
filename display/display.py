from matplotlib import pyplot
import networkx


# function that receives a list of nodes and a solution and plot the graph
def plot(node_list, solution):

    sample = len(node_list)

    # create graph
    graph = networkx.DiGraph()
    # add nodes
    graph.add_nodes_from(range(0, sample))

    # add edges from solution
    edges = []
    for i in solution:
        if i == len(solution) - 1:
            edges.append((solution[i], solution[0]))
        else:
            edges.append((solution[i], solution[i + 1]))
    graph.add_edges_from(edges)

    # get coordinates and labels of every node
    coord = {}
    for idx, node in enumerate(node_list):
        coord[idx] = (node[0], node[1])

    labels = {}
    for idx, node in enumerate(graph.nodes()):
        labels[node] = idx

    pyplot.figure(figsize=(10, 10))

    networkx.draw_networkx_nodes(graph, coord)
    networkx.draw_networkx_edges(graph, coord)
    networkx.draw_networkx_labels(graph, coord, labels, font_size=13)
    # networkx.draw_networkx(G, with_labels=True)

    pyplot.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
    pyplot.tick_params(axis='y', which='both', right=False, left=False, labelleft=False)
    for pos in ['right', 'top', 'bottom', 'left']:
        pyplot.gca().spines[pos].set_visible(False)

    pyplot.show()
