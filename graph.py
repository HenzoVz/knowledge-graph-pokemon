import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def main(type1, type2):
    triplas = []
    data = pd.read_csv("data/datasets_121_280_Pokemon.csv")
    data.replace(np.nan, 'NaN', inplace=True)
    for idx, row in data.iterrows():
        if row['Type 2'] == 'NaN':
            row['Type 2'] = row['Type 1']
        triplas.append((row['Name'], row['Type 1'], row['Type 2']))

    G = nx.Graph()
    for tripla in triplas:
        if tripla[1] == type1 and (tripla[2] == type2 or tripla[2] == type1):
            G.add_node(tripla[0]) # Name
            G.add_node(tripla[1]) # Type 1
            G.add_node(tripla[2]) # Type 2
            G.add_edge(tripla[0], tripla[1])
            G.add_edge(tripla[0], tripla[2])
    pos = nx.spring_layout(G)
    nx.draw(G, pos, edge_color='black', width=1, linewidths=1,
                    node_size=500, alpha=0.9,
                    labels={node: node for node in G.nodes()})

    plt.show()

if __name__ == '__main__':
    main('Grass', 'Poison')
    main('Fire', 'Flying')


