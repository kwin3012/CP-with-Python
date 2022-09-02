class BSTNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right
    
# the bst is build with consisderation that the equal values of node  will be on left side of node.
class BST:
    def __init__(self):
        self.root = None

    def insert(self,val):
        if self.root is None:
            self.root = BSTNode(val)
        else:
            prev = None
            curr = self.root
            while(curr is not None):
                if val <= curr.val:
                    prev = curr
                    curr = curr.left
                else:
                    prev = curr
                    curr = curr.right
            if val <= prev.val:
                prev.left = BSTNode(val)
            else:
                prev.right = BSTNode(val)

    def check(self,val):
        curr = self.root
        while(curr is not None):
            if val<curr.val:
                curr = curr.left
            elif val==curr.val:
                return True
            else:
                curr = curr.right
        
        return False

    # this will work only for unique values in trees.
    def remove(self,val):
        prev = None
        curr = self.root
        while(curr is not None):
            if val<curr.val:
                curr = curr.left
            elif val>curr.val:
                curr = curr.right
            else:
                # delete this node will and push right side of this node to curr node position
                # we needs to work on it.
                pass
                

bst = BST()

for i in range(10):
    bst.insert(i)


print(bst.check(0))
print(bst.check(1))
print(bst.check(4))
print(bst.check(10))
print(bst.root.right.val) 



                



        