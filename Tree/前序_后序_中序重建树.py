"""
前序 中序 
前序：1245367   中序：4251637
构建树时， 我们首先找到根节点的位置，然后找出左子树的前序遍历， 中序遍历赋给根节点的左孩子， 同理赋给根节点的右孩子
时间复杂度o(n)， n是结点个数， 因为每一个节点都需要成为root
空间复杂度:o(k)， k是树的深度，返回的答案也需要o(n)的空间
"""
def buildTree1(preorder, inorder):
    if not preorder or not inorder:
        return None
    
    root = TreeNode(preorder[0])
    index = inorder.index(root.val)
    root.left = buildTree1(preorder[1:1+index], inorder[:index])
    root.right = buildTree1(preorder[index+1:], inorder[index+1:])
    return root

"""
中序 后序 同理， 只是每次遍历的根节点在后序遍历的末尾
中序：4251637   后序：4526731
"""
def buildTree2(inorder, postorder):
    if not inorder or not postorder:
        return None
    root = TreeNode(postorder[-1])
    index = inorder.index(root.val)

    root.left = buildTree2(inorder[:index], postorder[index+1:])
    root.right = buildTree2(inorder[:index], postorder[index:-1])
    return root


"""
中序 后序 遍历时根节点在前序的第一个和后序的最后一个， 前序遍历是[根节点][左子树的根节点+左子树的前序遍历][右子树的根节点+右子树的前序遍历]
后序遍历是[左子树的后序遍历 左子树的根节点] + [右子树的后序遍历 右子树的根节点] + 根节点
所以前序遍历的第二个数字就是左子树的根节点， 左子树的个数就是后序遍历中从第一个数到左子树根节点的位置
"""

def buildTree3(preorder, postorder):
    if not preorder or not postorder:
        return  None
    root = TreeNode(preorder[0])
    if len(preorder) == 1:
        return root
    index = postorder.index(preorder[1])
    root.left = buildTree3(preorder[1:2+index], postorder[:index+1])
    root.right = buildTree3(preorder[2+index:], postorder[index+1:-1])
    return root