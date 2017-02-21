"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""

def postOrder(root):
    #Write your code here
    nodeStack = []
    resultItems = []
    # Print nodes till the first unevaluated right
    while True:
        buildStack(root, nodeStack)
        if len(nodeStack) == 0:
            break
        root = popAndGoRight(nodeStack, resultItems)
    print(" ".join(resultItems))
        
def buildStack(root, nodeStack):
    
    # Going to the deepest node on the left with
    # right pointers on stack
    while root != None:
        if root.right != None:
            nodeStack.append(root.right)
        nodeStack.append(root)
        root = root.left
        
def popAndGoRight(nodeStack, resultItems):
    
    # Pop leaf Nodes and take out right child
    # and process it
    
    while len(nodeStack) > 0:
        current = nodeStack.pop()
        if len(nodeStack) == 0:
            resultItems.append(str(current.data))
            return None
        if current.right is not None and current.right == nodeStack[-1]:
            right = nodeStack.pop()
            root = right
            nodeStack.append(current)
            return root
        resultItems.append(str(current.data))
        return None
