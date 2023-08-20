import networkx as nx
import matplotlib.pyplot as plt

def draw_transition_diagram():
    # Create a directed graph
    G = nx.DiGraph()

    # Add states to the graph
    states = ['S0', 'S1', 'ERROR']
    for state in states:
        G.add_node(state)

    # Define transitions
    # From S0, if it's a letter or _, go to S1. Else, go to ERROR state.
    G.add_edge('S0', 'S1', label='a-zA-Z_')
    G.add_edge('S0', 'ERROR', label='other')

    # From S1, if it's a letter, number, or _, stay in S1. Else, go to ERROR state.
    G.add_edge('S1', 'S1', label='a-zA-Z0-9_')
    G.add_edge('S1', 'ERROR', label='other')

    # Draw the graph
    pos = nx.spring_layout(G)
    plt.figure(figsize=(10, 6))

    nx.draw(G, pos, with_labels=True, node_size=3000, node_color='skyblue', font_size=15, width=2, edge_color='gray')
    edge_labels = nx.get_edge_attributes(G, 'label')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=12)

    plt.title("Transition Diagram for Variable Names")
    plt.show()

draw_transition_diagram()
