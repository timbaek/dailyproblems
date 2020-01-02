def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
  return self.search_tree(s,t)
    
def search_tree(self, node, root):
  if node:
      if node.val == root.val:
          if self.check_same_tree(node, root):
              return True
      
      left = self.search_tree(node.left, root)
      right = self.search_tree(node.right, root)
      
      return (left or right)
  else:
      return False
    
def check_same_tree(self, n, m):
  if (n and not m) or (m and not n):
      return False
  if not (n and m):
      return True
  if n.val != m.val:
      return False
  else:
      return self.check_same_tree(n.left,m.left) and self.check_same_tree(n.right, m.right)
