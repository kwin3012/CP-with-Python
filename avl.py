
import sys
from sys import stdin
input = stdin.readline

sys.setrecursionlimit(10**5)

class TreeNode:
    def __init__(self, val):
        self.count = 1    # assigning count variable so that during insertion in will be incremented for duplicate values
        # and during deletion, it will be decremented if has multiple copies.
        self.height = 1
        self.val = val
        self.left = None
        self.right = None
        self.lc = 0
        self.rc = 0
# only insertion and deletion will be affected. if multiple copies are there, entry(count) will be printed during traversal.
 
# AVL tree class which supports insertion,
# deletion operations
 
 
class AVL_Tree:
 
    def insert(self, root, key):
 
        # Step 1 - Perform normal BST
        if not root:
            return TreeNode(key)
        elif key < root.val:
            root.left = self.insert(root.left, key)
        elif key > root.val:
            root.right = self.insert(root.right, key)
        else:
            root.count += 1  # incrementing count if same entry is inserted.
 
        # Step 2 - Update the height of the
        # ancestor node
        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))
                              
        root.rc = self.getLc(root.right) + self.getCount(root.right) + self.getRc(root.right)
        root.lc = self.getLc(root.left) + self.getCount(root.left) + self.getRc(root.left)
 
        # Step 3 - Get the balance factor
        balance = self.getBalance(root)
 
        # Step 4 - If the node is unbalanced,
        # then try out the 4 cases
        # Case 1 - Left Left
        if balance > 1 and key < root.left.val:
            return self.rightRotate(root)
 
        # Case 2 - Right Right
        if balance < -1 and key > root.right.val:
            return self.leftRotate(root)
 
        # Case 3 - Left Right
        if balance > 1 and key > root.left.val:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
 
        # Case 4 - Right Left
        if balance < -1 and key < root.right.val:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
 
        return root
 
    # Recursive function to delete a node with
    # given key from subtree with given root.
    # It returns root of the modified subtree.
    def delete(self, root, key):
 
        # Step 1 - Perform standard BST delete
        if not root:
            return root
 
        elif key < root.val:
            root.left = self.delete(root.left, key)
 
        elif key > root.val:
            root.right = self.delete(root.right, key)
 
        else:
            if root.count > 1:  # if count is more than one i.e multiple copies are there
                root.count -= 1  # just decrement count
                return root   # so that one copy will be deleted and return
 
            if root.left is None:
                temp = root.right
                root = None
                return temp
 
            elif root.right is None:
                temp = root.left
                root = None
                return temp
 
            temp = self.getMinValueNode(root.right)
            root.val = temp.val
            root.right = self.delete(root.right,
                                     temp.val)
 
        # If the tree has only one node,
        # simply return it
        if root is None:
            return root
 
        # Step 2 - Update the height of the
        # ancestor node
        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))
                              
        root.rc = self.getLc(root.right) + self.getCount(root.right) + self.getRc(root.right)
        root.lc = self.getLc(root.left) + self.getCount(root.left) + self.getRc(root.left)
 
        # Step 3 - Get the balance factor
        balance = self.getBalance(root)
 
        # Step 4 - If the node is unbalanced,
        # then try out the 4 cases
        # Case 1 - Left Left
        if balance > 1 and self.getBalance(root.left) >= 0:
            return self.rightRotate(root)
 
        # Case 2 - Right Right
        if balance < -1 and self.getBalance(root.right) <= 0:
            return self.leftRotate(root)
 
        # Case 3 - Left Right
        if balance > 1 and self.getBalance(root.left) < 0:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
 
        # Case 4 - Right Left
        if balance < -1 and self.getBalance(root.right) > 0:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
 
        return root
 
    def leftRotate(self, z):
 
        y = z.right
        T2 = y.left
 
        # Perform rotation
        y.left = z
        z.right = T2
 
        # Update heights
        z.height = 1 + max(self.getHeight(z.left),
                           self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                           self.getHeight(y.right))
                           
        z.rc = self.getLc(z.right) + self.getCount(z.right) + self.getRc(z.right)
        z.lc = self.getLc(z.left) + self.getCount(z.left) + self.getRc(z.left)
        
        y.rc = self.getLc(y.right) + self.getCount(y.right) + self.getRc(y.right)
        y.lc = self.getLc(y.left) + self.getCount(y.left) + self.getRc(y.left)
 
        # Return the new root
        return y
 
    def rightRotate(self, z):
 
        y = z.left
        T3 = y.right
 
        # Perform rotation
        y.right = z
        z.left = T3
 
        # Update heights
        z.height = 1 + max(self.getHeight(z.left),
                           self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                           self.getHeight(y.right))
                           
        z.rc = self.getLc(z.right) + self.getCount(z.right) + self.getRc(z.right)
        z.lc = self.getLc(z.left) + self.getCount(z.left) + self.getRc(z.left)
        
        y.rc = self.getLc(y.right) + self.getCount(y.right) + self.getRc(y.right)
        y.lc = self.getLc(y.left) + self.getCount(y.left)+ self.getRc(y.left)
 
        # Return the new root
        return y
 
    def getHeight(self, root):
        if not root:
            return 0
 
        return root.height
        
    def getLc(self,root):
        if not root:
            return 0
        return root.lc
        
        
    def getRc(self,root):
        if not root:
            return 0
        return root.rc
    
    def getCount(self,root):
        if not root:
            return 0
        return root.count
    
    def getBalance(self, root):
        if not root:
            return 0
 
        return self.getHeight(root.left) - self.getHeight(root.right) #??
 
    def getMinValueNode(self, root):
        if root is None or root.left is None:
            return root
 
        return self.getMinValueNode(root.left)
 
    def preOrder(self, root):
 
        if not root:
            return
 
        print(root.val,root.lc,root.count,root.rc," ",end=" - ")
        self.preOrder(root.left)
        self.preOrder(root.right)

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))

    tree = AVL_Tree()
    root = None
    ans = 0
    for num in a:
        curr = root
        num_g = 0
        while(curr is not None):
            if num>=curr.val:
                curr = curr.right
            else:
                num_g += curr.count+curr.rc
                curr = curr.left
                
        curr = root
        num_l = 0
        
        while(curr is not None):
            if num<=curr.val:
                curr = curr.left
            else:
                num_l += curr.count+curr.lc
                curr = curr.right
                
        root = tree.insert(root, num)
        # tree.preOrder(root)
        
        ans += min(num_l,num_g)
        # print(ans,"ans")
        # print("-------") 
    print(ans)

    
        
        
    
    
    
    
    
    
