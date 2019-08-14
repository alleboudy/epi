from test_framework import generic_test
from bst_node import BstNode



#just insterting the nodes  nlogn

# def insertNodeInTree(root,nodeVal):

#     parent = root
#     isRight = False
#     while root:
#         parent = root
#         if root.data > nodeVal:
#             isRight = False
#             root = root.left
#         else:
#             isRight=True
#             root = root.right

#     if isRight:
#         parent.right = BstNode(nodeVal)
#     else:
#         parent.left =  BstNode(nodeVal)





# def rebuild_bst_from_preorder(preorder_sequence):
    
#     if len(preorder_sequence)==0:
#         return None

    
#     root = BstNode(preorder_sequence[0])
#     i=1
#     while i < len(preorder_sequence):
#         insertNodeInTree(root,preorder_sequence[i])
#         i+=1
#     return root



## recusrive, worest case n2



def rebuild_bst_from_preorder(preorder_sequence):
    if not preorder_sequence:
        return None

    tp = next((i for i,a in enumerate(preorder_sequence) if a > preorder_sequence[0]),len(preorder_sequence))

    return BstNode(
        preorder_sequence[0],
        rebuild_bst_from_preorder(preorder_sequence[1:tp]),
        rebuild_bst_from_preorder(preorder_sequence[tp:])

        )
    

    return root






# def rebuild_bst_from_preorder(preorder_sequence):
    
#     if len(preorder_sequence) == 0:
#         return None
#     root = None
#     i=0
#     status = 0  #0=up, 1 = left, 2=right 

#     while i < len(preorder_sequence):
#         if status == 0:#we are building a root
#             newRoot = BstNode(preorder_sequence[i])
#             if root is None:#fisrt time
#                 root = newRoot
#                 status = 1
#             else:
#                 newRoot.left = root
#                 root = newRoot
#                 status  = 2
            
#         elif status==1:
#             root.left = BstNode(preorder_sequence[i])
#             status = 2
#         else:
#             root.right = BstNode(preorder_sequence[i])
#             status = 0
#         i+=1
#     return root






if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("bst_from_preorder.py",
                                       'bst_from_preorder.tsv',
                                       rebuild_bst_from_preorder))
