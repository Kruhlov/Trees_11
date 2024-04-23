# Pre-order traversal
def pre_order(node):  
    str=[]
    if node is not None:
        str.append(node.data)
        str+=pre_order(node.left)
        str+=pre_order(node.right)
    return str

# In-order traversal
def in_order(node):
    str=[]
    if node is not None:
        str+=in_order(node.left)
        str.append(node.data)
        str+=in_order(node.right)
    return str

# Post-order traversal
def post_order(node):
    str=[]
    if node is not None:
        str+=post_order(node.left)
        str+=post_order(node.right)
        str.append(node.data)
    return str
