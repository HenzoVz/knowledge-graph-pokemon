import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def show_graph_by_type(type1, type2):

    triplas = []
    data = pd.read_csv("data/datasets_121_280_Pokemon.csv")
    data.replace(np.nan, 'NaN', inplace=True)
    for idx, column in data.iterrows():
        if column['Type 1'] == type1 and column['Type 2'] == type2:
            triplas.append((column['Name'], column['Type 1'], column['Type 2']))

    G = nx.Graph()
    for tripla in triplas:
        if tripla[2] == 'NaN':
            continue
        G.add_node(tripla[0]) # Name
        G.add_node(tripla[1]) # Type 1
        G.add_node(tripla[2]) # Type 2
        G.add_edge(tripla[0], tripla[1])
        G.add_edge(tripla[0], tripla[2])
    pos = nx.spring_layout(G)
    nx.draw(G, pos, edge_color='black', width=1, linewidths=1,
                    node_size=500, alpha=0.9,
                    labels={node: node for node in G.nodes()}, arrows=True)
    plt.show()


show_graph_by_type('Grass', 'Poison')

