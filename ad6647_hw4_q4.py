from LinkedBinaryTree import LinkedBinaryTree

def min_and_max(bin_tree):
    if bin_tree.is_empty() == True:
        raise Exception("Tree is empty")
    def subtree_min_and_max(root):
        if root is None:
            return float('inf'), float('-inf')
        left_min, left_max = subtree_min_and_max(root.left)
        right_min, right_max = subtree_min_and_max(root.right)
        current_min = min(root.data, left_min, right_min)
        current_max = max(root.data, left_max, right_max)
        return current_min, current_max
    return subtree_min_and_max(bin_tree.root)