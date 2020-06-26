
num_of_nodes = 0
class bt_node:
    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None
        global num_of_nodes
        num_of_nodes += 1
        
root = bt_node(1)
root.right = bt_node(2)
root.right.right = bt_node(5)
root.right.right.left = bt_node(3)
root.right.right.right = bt_node(6)
root.right.right.left.right = bt_node(4)

"""
Algorithm:
1. Set the index i = 0. Visit the root node and appends to BFS (Queue) array, if root is none return Empty arrray
2. Take the node at 'i'th index in the Queue
3. If that node has left child and it is not visited yet, append it to the BFS Queue.
4. If that node has right child and it is not visited yet, append it to the BFS Queue.
5. Increment the index i, to visit the next node in the BFS Queue.
6. If the number of nodes visited equals to the total number of nodes in the tree(including root),
exit from the loop and return the BFS Queue as result.
7. Else, goto Step2 and repeat.
"""

def bfs_traversal(root):
    if root:
        global num_of_nodes
        bfs = []
        bfs.append(root)
        i = 0
        while True:
            beg = bfs[i]
            if beg.left and beg.left not in bfs:
                bfs.append(beg.left)
            if beg.right and beg.right not in bfs:
                bfs.append(beg.right)
            i += 1
            if num_of_nodes == i+1:
                break
        print('->'.join([str(x.value) for x in bfs]))
    else:
        print('Empty binary tree ')
    """
    Resetting the varaibles
    """
    num_of_nodes = 0
    bfs.clear()
bfs_traversal(root)
