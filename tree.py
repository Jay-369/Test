class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child):
        self.children.append(child)

# Creating a tree
root = TreeNode("Root")


child1 = TreeNode("Child 1")
child2 = TreeNode("Child 2")

root.add_child(child1)
root.add_child(child2)

ch=root.children
print(ch[0].data)
print(ch[1].data)
print(root.data)