from test_framework import generic_test, test_utils







def find_k_largest_in_bst(root, k):
    res = []
    def tree_desc(root):
        if root and len(res)<k:
            tree_desc(root.right)
            if len(res)<k:
                res.append(root.data)
                tree_desc(root.left)
        

    tree_desc(root)
    return res






    


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "k_largest_values_in_bst.py", 'k_largest_values_in_bst.tsv',
            find_k_largest_in_bst, test_utils.unordered_compare))
#     return tree_desc(tree)[-k:]
