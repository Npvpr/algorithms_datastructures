import matplotlib.pyplot as plt
import networkx as nx

def plot_hierarchical_tree(root, title="Binary Tree"):
    """
    Enhanced hierarchical tree visualization
    Usage: visualize_tree.plot_hierarchical_tree(root_node, "My Tree Title")
    """
    nodes = {}
    edges = []
    
    def traverse(node, node_id='0', level=0, pos=0):
        if node:
            # Add this node to our nodes dictionary
            nodes[node_id] = {
                'value': node.value,
                'level': level,
                'pos': pos
            }
            
            # Process left child
            if node.left:
                left_id = f"{node_id}L"
                edges.append((node_id, left_id))
                traverse(node.left, left_id, level + 1, pos - 2**(4-level))
                
            # Process right child
            if node.right:
                right_id = f"{node_id}R"
                edges.append((node_id, right_id))
                traverse(node.right, right_id, level + 1, pos + 2**(4-level))
    
    traverse(root)
    
    # Create a directed graph
    G = nx.DiGraph()
    
    # Add nodes with positions
    for node_id, data in nodes.items():
        G.add_node(node_id, value=data['value'], pos=(data['pos'], -data['level']))
    
    # Add edges
    G.add_edges_from(edges)
    
    # Get node positions from the graph
    pos = nx.get_node_attributes(G, 'pos')
    
    # Create figure
    plt.figure(figsize=(12, 8))
    plt.title(title)
    
    # Draw nodes
    nx.draw_networkx_nodes(G, pos, 
                          node_color='skyblue', 
                          node_size=700,
                          node_shape='o')
    
    # Draw edges
    nx.draw_networkx_edges(G, pos, arrows=False, width=1.5)
    
    # Draw labels
    labels = {node: data['value'] for node, data in G.nodes(data=True)}
    nx.draw_networkx_labels(G, pos, labels=labels, font_size=12)
    
    plt.axis('off')
    plt.tight_layout()

    plt.show()