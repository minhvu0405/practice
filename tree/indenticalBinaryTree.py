# Given two binary trees, write a function to check if they are equal or not.
#
# Two binary trees are considered equal if they are structurally identical and the nodes have the same value.
#
# Return 0 / 1 ( 0 for false, 1 for true ) for this problem
#
# Example :
#
# Input :
#
#    1       1
#   / \     / \
#  2   3   2   3
#
# Output :
#   1 or True
def isSameTree(A, B):
    if A is None and B is None:
        return 1
    if A is None or B is None:
        return 0
    if A.val == B.val and isSameTree(A.left,B.left) and isSameTree(A.right,B.right):
        return 1
    return 0