"""用python实现深度优先搜索，
    创建图类，图节点类
    最后dfs_search为实现算法主函数"""

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
        self.node_list = node_list


    def add_edge(self, node1, node2):
        """给在图内的2个节点添加边"""
        if node1 in self.node_list and node2 in self.node_list:
            node1.add_linkedNode(node2)
            node2.add_linkedNode(node1)


    def remove_edge(self, node1, node2):
        """给在图内相连节点关系去除"""
        if node1 in self.node_list and node2 in self.node_list:
            node1.remove_linkedNode(node2)
            node2.remove_linkedNode(node1)



def dfs_search(start_node, search_value):
    """利用深度优先搜索目标值"""
    visited_list = []

    #用列表存储堆栈数据结构
    stack = [start_node]

    #遍历数据
    while len(stack) > 0:
        cur_node = stack.pop()

        """对于深度优先搜索，若节点已经访问过，则直接结束，避免死循环"""
        if cur_node in visited_list:
            return

        print("current node value: ", cur_node.value)
        visited_list.append(cur_node) #将节点添加到访问过列表

        #若当前节点为目标节点，返回当前节点
        if cur_node.value == search_value:
            return cur_node

        #若不是目标节点，采用堆栈结构添加当前节点临近节点---深度优先搜索
        for ele in cur_node.linkedNode:
            if ele not in visited_list:
                stack.append(ele)

    return None


"""测试"""
nodeG = GraphNode('G')
nodeR = GraphNode('R')
nodeA = GraphNode('A')

graph = Graph([nodeG, nodeA, nodeR])
graph.add_edge(nodeG, nodeR)
graph.add_edge(nodeA, nodeR)

result = dfs_search(nodeG, 'U')
if result:
    print("you got it! ", result.value)
else:
    print('None')
