from test_framework import generic_test


def inorder_traversal(tree):
    
    if not tree:
        return []
    
    return inorder_traversal(tree.left) + [tree.data] +inorder_traversal(tree.right)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_inorder.py", 'tree_inorder.tsv',
                                       inorder_traversal))
