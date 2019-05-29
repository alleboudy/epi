from test_framework import generic_test


def is_balanced_binary_tree(tree):
    
    def check_balance(tree):
        if not tree:
            return (True,-1)
        left = check_balance(tree.left)
        if not left[0]:
            return (False,0)
        right = check_balance(tree.right)
        if not right[0]:
            return (False,0)
        
        is_balanced = abs(left[1]-right[1])<=1
        height = max(left[1],right[1]) + 1
        return (is_balanced,height)
    return check_balance(tree)[0]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_balanced.py",
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
