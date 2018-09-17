# -*- coding=utf-8 -*-

import suffix_expression

class Node:
    """
    二叉树的结点
    """
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def generate_binary_tree(exp):
    """
    生成二叉树
    """
    tree_stack = []
    for item in exp:
        #print(item)
        parent = Node(item)
        if not item in  ['+', '-', 'x', '÷']:
            #操作数
            tree_stack.append(parent)
        else:
            #运算符
            right = tree_stack.pop()
            left = tree_stack.pop()
            parent.right = right
            parent.left = left
            tree_stack.append(parent)
    #二叉树的根
    parent = tree_stack[-1]
    return parent

def tree_is_same(root):
    """
    判断二叉树是否相同
    """
    pass

if __name__ == '__main__':
    exp = '9 + ( 3 - 1 ) x 3 + 10 ÷ 2'
    re = suffix_expression.to_suffix(exp)
    #print(re)
    res = generate_binary_tree(re)
    print(res.value)