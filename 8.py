import networkx as nx
import matplotlib.pyplot as plt

def read_graph_from_file(filename):
    G = nx.Graph()
    with open(filename, 'r') as file:
        for line in file:
            nodes = line.strip().split()
            if len(nodes) == 2:
                G.add_edge(nodes[0], nodes[1])
    return G

def plot_graph(G, colors=None, subplot=None):
    pos = nx.planar_layout(G)
    nx.draw(G, pos, with_labels=True, node_color=colors, node_size=500, font_size=12, ax=subplot)
    if subplot is None:
        plt.axis('off')
        plt.show()

def color_graph(G):
    colors = ['red', 'green', 'blue', 'yellow']
    color_map = {}
    for node in G.nodes():
        used_colors = set(color_map.get(neighbor) for neighbor in G.neighbors(node))
        for color in colors:
            if color not in used_colors:
                color_map[node] = color
                break
    return [color_map.get(node) for node in G.nodes()]

# Чтение графа из файла
filename = 'graph.txt'
G = read_graph_from_file(filename)

# Раскраска графа
colors = color_graph(G)

# Создание фигуры с двумя подграфиками
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

# Вывод исходного графа
ax1.set_title("Исходный граф")
plot_graph(G, subplot=ax1)

# Вывод раскрашенного графа
ax2.set_title("Раскрашенный граф")
plot_graph(G, colors, subplot=ax2)

# Отключение осей и отображение графиков
plt.axis('off')
plt.tight_layout()
plt.show()
