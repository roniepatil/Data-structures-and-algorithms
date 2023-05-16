class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert_helper(self, new_val, current):
        if new_val > current.value:
            if current.right:
                self.insert_helper(new_val, current.right)
            else:
                current.right = Node(new_val)
        else:
            if current.left:
                self.insert_helper(new_val, current.left)
            else:
                current.left = Node(new_val)

    def insert(self, new_val):
        return self.insert_helper(new_val, self.root)

    def search_helper(self, val, current):
        if current:
            if val == current.value:
                return True
            elif val > current.value:
                return self.search_helper(val, current.right)
            else:
                return self.search_helper(val, current.left)
        else:
            return False


    def search(self, find_val):
        return self.search_helper(find_val, self.root)
    
# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
# Should be True
print(tree.search(4))
# Should be False
print(tree.search(6))