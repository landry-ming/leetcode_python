"""
disjoint set union(DSU)
1. 判断node1和node2是否相连， 就是判断两者的root node是否相同
2. 如果两者不相连， 就把连着的root node相连
"""

class DSU:
    
    def __init__(self, number):
        self.node_connect_list = [-1] * (number+1)
    
    def root_node_find(self, node):
        while self.node_connect_list[node] != -1:
            node = self.node_connect_list[node]
        return node
    
    def node_connected(self, node1, node2):
        node1_root = self.root_node_find(node1)
        node2_root = self.root_node_find(node2)
        if node1_root == node2_root:
            print('connected')
        else:
            self.node_connect_list[node1_root] = node2_root
dsu = DSU(4)
dsu.node_connected(1, 3)
dsu.node_connected(1, 2)

print(dsu.node_connect_list)


