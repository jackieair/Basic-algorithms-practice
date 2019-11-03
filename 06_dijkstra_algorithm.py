"""用python实现迪克斯特拉最短路径搜索，
    创建边-节点类，图类，图节点类
    最BFS_search为实现算法主函数
    注意：不够完善--距离"""

import math


class GraphEdgeToNode:
    def __init__(self, node, distance):
        self.dest_node = node #目标节点
        self.distance = distance #到目标节点距离


class GraphNode:
    """定义图节点类，包含节点值以及节点相邻节点"""
    def __init__(self, value):
        self.value = value
        self.edges = []


    def add_linkedNodebyEdge(self, dest_node, distance):
        """创建通过边链接节点"""
        self.edges.append(GraphEdgeToNode(dest_node, distance))


    def remove_linkedNodebyEdge(self, del_node):
        """创建删除指定节点方法"""
        if del_node in self.edges:
            self.edges.remove(del_node)



class Graph:
    """定义图类，包含节点及边"""
    def __init__(self, node_list):
        self.nodes = node_list


    def add_edgeAndNode(self, from_node1, to_node2, distance):
        """给在图内的2个节点添加边、距离"""
        if from_node1 in self.nodes and to_node2 in self.nodes:
            from_node1.add_linkedNodebyEdge(to_node2, distance)
            to_node2.add_linkedNodebyEdge(from_node1, distance)


    def remove_edgeAndnode(self, from_node1, to_node2):
        """给在图内相连节点关系去除"""
        if from_node1 in self.nodes and to_node2 in self.nodes:
            from_node1.remove_linkedNodebyEdge(to_node2)
            to_node2.remove_linkedNodebyEdge(from_node1)



def dijkstra(graph, start_node, end_node):
    """实现迪克斯特拉算法"""

    distance_dict = {node : math.inf for node in graph.nodes} #关键设置，令位置节点距离为无穷
    shortest_path_to_node = []

    distance_dict[start_node] = 0

    while len(distance_dict) > 0:
        """按照字典里的距离进行排序，取最小节点信息对——节点及距离"""
        cur_node, cur_distance = sorted(distance_dict.items(), key = lambda x: x[1])[0]

        #将第一个节点信息存到路径列表中
        shortest_path_to_node.append([cur_node.value, distance_dict.pop(cur_node)])

        """遍历每个节点连接的边"""
        for edge in cur_node.edges:
            dest_node = edge.dest_node

            """dict中存储所有节点，若不在节点则是之前pop出来了
                迪克斯特拉算法默认访问过的节点为最短路径，所以pop过后不管"""
            if dest_node in distance_dict:
                new_node_distance = cur_distance + edge.distance

                #若新距离比原先短，则更新该节点距离
                if new_node_distance < distance_dict[dest_node]:
                    distance_dict[dest_node] = new_node_distance

    print(shortest_path_to_node)
    return shortest_path_to_node[-1][1]


"""测试"""
node_u = GraphNode('U')
node_d = GraphNode('D')
node_a = GraphNode('A')
node_c = GraphNode('C')
node_i = GraphNode('I')
node_t = GraphNode('T')
node_y = GraphNode('Y')

graph = Graph([node_u, node_d, node_a, node_c, node_i, node_t, node_y])
graph.add_edgeAndNode(node_u, node_a, 4)
graph.add_edgeAndNode(node_u, node_c, 6)
graph.add_edgeAndNode(node_u, node_d, 3)

graph.add_edgeAndNode(node_d, node_u, 3)
graph.add_edgeAndNode(node_d, node_c, 4)

graph.add_edgeAndNode(node_a, node_u, 4)
graph.add_edgeAndNode(node_a, node_i, 7)

graph.add_edgeAndNode(node_c, node_d, 4)
graph.add_edgeAndNode(node_c, node_u, 6)
graph.add_edgeAndNode(node_c, node_i, 4)
graph.add_edgeAndNode(node_c, node_t, 5)

graph.add_edgeAndNode(node_i, node_a, 7)
graph.add_edgeAndNode(node_i, node_c, 4)
graph.add_edgeAndNode(node_i, node_y, 4)

graph.add_edgeAndNode(node_t, node_c, 5)
graph.add_edgeAndNode(node_t, node_y, 5)

graph.add_edgeAndNode(node_y, node_i, 4)
graph.add_edgeAndNode(node_y, node_t, 5)

print('Shortest Distance from {} to {} is {}'.format(node_u.value, node_y.value, dijkstra(graph, node_u, node_y)))
