import matplotlib.pyplot as plt
import networkx as nx

try:
    import pygraphviz
    from networkx.drawing.nx_agraph import graphviz_layout
except ImportError:
    try:
        import pydot
        from networkx.drawing.nx_pydot import graphviz_layout
    except ImportError:
        raise ImportError("This example needs Graphviz and either "
                          "PyGraphviz or pydot")

G = nx.Graph()
G.add_node(1)
G.add_nodes_from([2, 3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18])

G.add_edge(1, 2)
G.add_edge(1, 3)

G.add_edge(2, 4)
G.add_edge(2, 5)
G.add_edge(3, 6)
G.add_edge(3, 7)
G.add_edge(3, 8)

G.add_edge(6, 9)
G.add_edge(6, 10)
G.add_edge(7, 11)
G.add_edge(7, 12)
G.add_edge(8, 13)
G.add_edge(8, 14)

G.add_edge(4, 16)
G.add_edge(4, 17)
G.add_edge(4, 18)

G.add_edge(5, 15)


pos = graphviz_layout(G, prog='twopi', args='')
plt.figure(figsize=(8, 8))
nx.draw(G, pos, node_size=20, alpha=0.5, node_color="blue", with_labels=False)
plt.axis('equal')
plt.show()