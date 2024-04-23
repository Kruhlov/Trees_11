from queue import Queue
def tree_by_levels(node):
    q=Queue()
    st=[]
    if node is not None:
        q.put(node)
    while not q.empty():
        n=q.get()
        if n.left is not None:
            q.put(n.left)
        if n.right is not None:
            q.put(n.right)
        st.append(n.value)
    return st
