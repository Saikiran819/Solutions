"""
1. Create a binary tree.
2. Traverse from root node to the target node1 and save the path in the array path1.
3. Traverse from root node to the target node2 and save the path in the array path2.
4. Traverse through the arrays path1 and path2, pop the nodes which are not equal.
5. Return the last two elements in the path1 or path2 which are the nearest common
parents or ancestors.

"""
class bt_node:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

def path_from_root_to_node(root, path, node):
    
	if not root:
		return 0

	path.append(root.value)

	if root.value == node:
		return 1

	if ((root.left and path_from_root_to_node(root.left, path, node)) or
		(root.right and path_from_root_to_node(root.right, path, node))): 
		return 1
	path.pop()
	return 0

def two_nearest_common_parents(root, n1, n2):
    path1 = []
    path2 = []
    i = 0
    if (not path_from_root_to_node(root, path1, n1) or 
        not path_from_root_to_node(root, path2, n2)):
        return -1

    path1 = path1[:-1]
    path2 = path2[:-1]
    while(i < len(path1) and i < len(path2)):
        if path1[i] != path2[i]:
            path1.pop(i)
            path2.pop(i)
        i += 1
    return path1[-1:-3:-1]

root = bt_node(2)
root.left = bt_node(1)
root.right = bt_node(3)
root.right.left = bt_node(4)
root.right.right = bt_node(5)
root.right.right.left = bt_node(6)

print (f'Two nearest common parents of 4, 5 are {two_nearest_common_parents(root, 4, 5,)}')
print (f'Two nearest common parents of 4, 6 are {two_nearest_common_parents(root, 4, 6)}')
print (f'Two nearest common parents of 3, 4 are {two_nearest_common_parents(root,3,4)}')
print (f'Two nearest common parents of 2, 4 are {two_nearest_common_parents(root,2, 4)}')