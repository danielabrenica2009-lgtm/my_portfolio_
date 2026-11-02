from flask import Blueprint, render_template

binary_tree_bp = Blueprint('binary_tree', __name__)

class Node:
    """A node in a binary tree."""
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BinaryTree:
    """A binary tree data structure."""
    def __init__(self, root_value=None):
        self.root = Node(root_value) if root_value is not None else None

    def insert_left(self, current_node, value):
        """Insert a node as the left child of the current node."""
        if current_node.left is None:
            current_node.left = Node(value)
        else:
            new_node = Node(value)
            new_node.left = current_node.left
            current_node.left = new_node

    def insert_right(self, current_node, value):
        """Insert a node as the right child of the current node."""
        if current_node.right is None:
            current_node.right = Node(value)
        else:
            new_node = Node(value)
            new_node.right = current_node.right
            current_node.right = new_node

    def preorder_traversal(self, start, traversal):
        """Traverse the tree in preorder (root, left, right)."""
        if start:
            traversal += (str(start.value) + " ")
            traversal = self.preorder_traversal(start.left, traversal)
            traversal = self.preorder_traversal(start.right, traversal)
        return traversal    

    def inorder_traversal(self, start, traversal):
        """Traverse the tree in inorder (left, root, right)."""
        if start:
            traversal = self.inorder_traversal(start.left, traversal)
            traversal += (str(start.value) + " ")
            traversal = self.inorder_traversal(start.right, traversal)
        return traversal    

    def postorder_traversal(self, start, traversal):
        """Traverse the tree in postorder (left, right, root)."""
        if start:
            traversal = self.postorder_traversal(start.left, traversal)
            traversal = self.postorder_traversal(start.right, traversal)
            traversal += (str(start.value) + " ")
        return traversal    

    def search(self, root, key):
        """Search for a specific value in the binary tree."""
        if root is None:
            return False
        if root.value == key:
            return True
        return self.search(root.left, key) or self.search(root.right, key)

    def delete_node(self, root, key):
        """Delete a node from the binary tree."""
        if root is None:
            return None
        
        if root.left is None and root.right is None:
            if root.value == key:
                return None
            return root

        queue = [root]
        key_node = None
        target_node = None
        last_node = None

        while queue:
            target_node = queue.pop(0)
            if target_node.value == key:
                key_node = target_node
            if target_node.left:
                last_node = target_node
                queue.append(target_node.left)
            if target_node.right:
                last_node = target_node
                queue.append(target_node.right)

        if key_node:
            x = target_node.value
            key_node.value = x
            if last_node:
                if last_node.right == target_node:
                    last_node.right = None
                elif last_node.left == target_node:
                    last_node.left = None
        return root


# Flask Route para sa Interactive Binary Tree View
@binary_tree_bp.route('/binary-tree')
def binary_tree_view():
    return render_template('binary_tree.html')


# Example usage
if __name__ == "__main__":
    tree = BinaryTree("R")
    tree.insert_left(tree.root, "A")
    tree.insert_right(tree.root, "B")
    tree.insert_left(tree.root.left, "C")
    tree.insert_right(tree.root.left, "D")
    tree.insert_left(tree.root.right, "E")
    tree.insert_right(tree.root.right, "F")
    tree.insert_left(tree.root.right.right, "G")
    
    print()
    print("Preorder traversal: " + tree.preorder_traversal(tree.root, ""))
    print("Inorder traversal: " + tree.inorder_traversal(tree.root, ""))
    print("Postorder traversal: " + tree.postorder_traversal(tree.root, ""))
    print("Search 'E':", tree.search(tree.root, "E"))
    print("Search 'Z':", tree.search(tree.root, "Z"))
    print()