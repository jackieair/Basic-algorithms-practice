"""深度优先搜索"""

class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


def preorder(root):
    """
    深度优先搜索之先序遍历
    遇到节点就记录并优先走左节点"""
    if not root:
        return None

    rsl = []  # 存结果
    stack = []  # 辅助堆
    node = root

    # 前向遍历
    while stack or node:
        while node:
            rsl.append(node)  # 在这记录
            stack.append(node)
            node = node.left

        # node为空跳出while循环
        node = stack.pop()
        node = node.right

    return rsl


def inorder(root):
    """
    深度优先搜索之中序遍历
    左-中-右"""
    if not root:
        return None

    stack, rsl = [], []
    node = root
    while stack or node:
        while node:
            stack.append(node)
            node = node.left

        node = stack.pop()
        rsl.append(node.val)  # 在这记录
        node = node.right
    return rsl


def postorder(root):
    """
    深度优先搜索之后序遍历
    左-右-中,稍微比中序要困难一些，有跳跃"""
    if not root:
        return None

    stack1, stack2, rsl = [], [], []
    node = root
    stack1 = [node]

    while stack1:
        # while循环找出后序遍历逆序，并存放在stack2中
        node = stack1.pop()
        if node.left:
            stack1.append(node.left)
        if node.right:
            stack1.append(node.left)
        # 存入stack2
        stack2.append(node)

    # 遍历stack2
    while stack2:
        node = stack.pop()
        rsl = append(node)  # 将逆序结果存入rsl中

    return rsl

