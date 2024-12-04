from LinkedBinaryTree import LinkedBinaryTree

def is_height_balanced(bin_tree):
    def check_balance(node):
        if node is None:
            return 0, True
        left_height, left_balanced = check_balance(node.left)
        right_height, right_balanced = check_balance(node.right)
        current_height = 1 + max(left_height, right_height)
        is_balanced = (abs(left_height - right_height) <= 1) and left_balanced and right_balanced
        return current_height, is_balanced
    _, is_balanced = check_balance(bin_tree.root)
    return is_balanced