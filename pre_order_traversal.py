"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""
import sys

output = []

def preOrder(root):
    #Write your code here
    if root == None:
        return
    output.append(str(root.data) + " ")
    preOrder(root.left)
    preOrder(root.right)

class Node():
    def __init__(self,data,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right

if __name__ == "__main__":
    t1 = Node(4, Node(5), Node(6))
    preOrder(t1)
    print(output)
