from test_framework import generic_test


def binary_tree_depth_order(tree):
    result = []
    if not tree:
        return result
    current_level = [tree]

    while current_level:
        result.append([c.data for c in current_level])
        current_level = [
            child for curr in current_level for child in (curr.left, curr.right) if child
        ]

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_level_order.py",
                                       "tree_level_order.tsv",
                                       binary_tree_depth_order))
