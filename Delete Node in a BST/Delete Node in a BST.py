class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if isinstance(root,TreeNode):
            if root.val==key:
                if not root.left: return root.right
                if not root.right: return root.left         
                if root.left and root.right:
                    node=root.right
                    while node.left:
                        node=node.left
                    root.val,root.right=node.val,self.deleteNode(root.right,node.val)
            elif root.val>key:
                root.left=self.deleteNode(root.left,key)
            else:
                root.right=self.deleteNode(root.right,key)
            return root
        return None
