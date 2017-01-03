# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
#
# Example :
#
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
# The above binary tree is symmetric.
# But the following is not:
#
#     1
#    / \
#   2   2
#    \   \
#    3    3
# Return 0 / 1 ( 0 for false, 1 for true ) for this problem
def isSymmetric(A):
    if A is None:
        return 1
    if checkMirror(A.left,A.right):
        return 1
    return 0
def checkMirror(left,right):
    if left is None and right is None:
        return 1
    if left is None or right is None:
        return 0
    if not (left.val == right.val and checkMirror(left.left,right.right)):
        return 0
    if not (left.val == right.val and checkMirror(left.right,right.left)):
        return 0
    return 1