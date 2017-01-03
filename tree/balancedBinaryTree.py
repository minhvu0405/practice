# Given a binary tree, determine if it is height-balanced.
#
# Height-balanced binary tree : is defined as a binary tree in which
# the depth of the two subtrees of every node never differ by more than 1.
# Return 0 / 1 ( 0 for false, 1 for true ) for this problem
#
# Example :
#
# Input :
#           1
#          / \
#         2   3
#
# Return : True or 1
#
# Input 2 :
#          3
#         /
#        2
#       /
#      1
#
# Return : False or 0
#          Because for the root node, left subtree has depth 2 and right subtree has depth 0.
#          Difference = 2 > 1.
def isBalanced(A):
    if A is None:
        return 1
    if getDepth(A) == -1:
        return 0
    return 1
def getDepth(A):
    if A is None:
        return 0
    left = getDepth(A.left)
    right = getDepth(A.right)
    if left == -1 or right == -1:
        return -1
    if abs(left - right) > 1:
        return -1
    return max(left,right) + 1