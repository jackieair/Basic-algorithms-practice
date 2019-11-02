"""用python实现广度优先搜索，
    创建图类，图节点类
    最BFS_search为实现算法主函数"""

class GraphNode:
    """定义图节点类，包含节点值以及节点相邻节点"""
    def __init__(self, value):
        self.value = value
        self.linkedNode = []

    def add_linkedNode(self, new_node):
        """创建添加节点方法"""
        self.linkedNode.append(new_node)

    def remove_linkedNode(self, del_node):
        """创建删除指定节点方法"""
        if del_node in self.linkedNode:
            self.linkedNode.remove(del_node)


class Graph:
    """定义图类，包含节点及边"""
    def __init__(self, node_list):
        self.nodes = node_list


    def add_edge(self, node1, node2):
        """给在图内的2个节点添加边"""
        if node1 in self.nodes and node2 in self.nodes:
            node1.add_linkedNode(node2)
            node2.add_linkedNode(node1)


    def remove_edge(self, node1, node2):
        """给在图内相连节点关系去除"""
        if node1 in self.nodes and node2 in self.nodes:
            node1.remove_linkedNode(node2)
            node2.remove_linkedNode(node1)


def bfs_search(start_node, search_value):
    """广度优先搜索"""

    visited_list = []
    queue = [start_node]

    while len(queue) > 0:
        """遍历节点，由于采用广度优先搜索————利用队列数据结构，故pop(0)"""
        cur_node = queue.pop(0)
        print("current poped node: ", cur_node)

        if cur_node in visited_list:
            return

        visited_list.append(cur_node)

        if cur_node.value == search_value:
            return cur_node

        for ele in cur_node.linkedNode:
            if ele not in visited_list:
                queue.append(ele)

    return None

"""测试"""
nodeG = GraphNode('G')
nodeR = GraphNode('R')
nodeA = GraphNode('A')

graph = Graph([nodeG, nodeA, nodeR])
graph.add_edge(nodeG, nodeR)
graph.add_edge(nodeA, nodeR)

result = bfs_search(nodeG, 'U')
if result:
    print("you got it! ", result.value)
else:
    print('None')
