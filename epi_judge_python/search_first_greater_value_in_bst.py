from test_framework import generic_test

def find_first_greater_than_k(tree, k):
    if tree is None:
        return None
    candidate = left = right = None
    if tree.data>k:
        candidate = tree 
        left = find_first_greater_than_k(tree.left, k)
        if left :
            return left
        else:
            return tree
    else:
        right = find_first_greater_than_k(tree.right, k)
        if right :
            return right
    return candidate

    # candidate = None
    # while tree:
    #     if tree.data>k:
    #         candidate,tree = tree,tree.left
    #     else:
    #         tree=tree.right
    # return candidate



def find_first_greater_than_k_wrapper(tree, k):
    result = find_first_greater_than_k(tree, k)
    return result.data if result else -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("search_first_greater_value_in_bst.py",
                                       'search_first_greater_value_in_bst.tsv',
                                       find_first_greater_than_k_wrapper))
