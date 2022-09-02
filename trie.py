class Node:
    def __init__(self):
        self.a = [None]*26
        self.flag = False
        
# have insert, ispresent and isstartwith function implemented
class Trie:
    def __init__(self):
        self.root = Node()
        
    def insert(self,s):
        node = self.root
        for i in range(len(s)):
            #check whether the reference is there or not
            if node.a[ord(s[i])-97] is None:
                node.a[ord(s[i])-97] = Node()
            
            # move forward the reference
            node = node.a[ord(s[i])-97]
            
        # setting the flag for ending node to be True
        node.flag = True
        
    def search(self,s):
        node = self.root
        for i in range(len(s)):
            # check whether an element is present or not
            if node.a[ord(s[i])-97] is None:
                return False
            
            #move forward
            node = node.a[ord(s[i])-97]
            
        
        # check for the complete word
        if node.flag == True:
            return True
        else:
            return False
            
    def startswith(self,s):
        node = self.root
        for i in range(len(s)):
            if node.a[ord(s[i])-97] is None:
                return False
            node = node.a[ord(s[i])-97]
        
        # no need to check for end
        return True
            
            
t = Trie()
t.insert("apple")
t.insert("apps")
t.insert("bat")
t.insert("apxl")
t.insert("bac")

print(t.search("apple"))
print(t.search("appl"))
print(t.search("tia"))
print(t.search("apps"))
print(t.search("batbac"))
print("------------")
print(t.startswith("apple"))
print(t.startswith("appl"))
print(t.startswith("tia"))
print(t.startswith("apps"))
print(t.startswith("batbac"))


######################################### Trie ##################################################

# have insert, erase, ispresent_count and isstartwith_count function implemented
class Node:
    def __init__(self):
        self.a = [None]*26
        self.flag = False
        self.count = 0
        
class Trie:
    def __init__(self):
        self.root = Node()
        
    def insert(self,s):
        node = self.root
        for i in range(len(s)):
            if node.a[ord(s[i])-97] is None:
                node.a[ord(s[i])-97] = Node()
            # node.b[ord(s[i])-97] += 1
            
            node = node.a[ord(s[i])-97]
            # Note we are storing info about the current node in the next node.
            node.count += 1
        node.flag = True
        
    def erase(self,s):
        node = self.root
        for i in range(len(s)):
            if node.a[ord(s[i])-97].count != 0:
                node.a[ord(s[i])-97].count -= 1
                
                if node.a[ord(s[i])-97].count == 0:
                    # if 0 changing the None and moving forward
                    temp = node.a[ord(s[i])-97]
                    node.a[ord(s[i])-97] = None
                    node = temp
                else:
                    # moving forward the node
                    node = node.a[ord(s[i])-97]
                    
    def search(self,s):
        node = self.root
        for i in range(len(s)):
            # check whether an element is present or not
            if node.a[ord(s[i])-97] is None:
                return False
            
            #move forward
            node = node.a[ord(s[i])-97]
            
        
        # check for the complete word
        if node.flag == True:
            return True
        else:
            return False
            
    def count_complete(self,s):
        node = self.root
        for i in range(len(s)):
            # check whether an element is present or not
            if node.a[ord(s[i])-97] is None:
                return 0
            
            #move forward
            node = node.a[ord(s[i])-97]
            
        # check for the complete word
        if node.flag == True:
            return node.count
        else:
            return 0
            
    def count_startwith(self,s):
        node = self.root
        for i in range(len(s)):
            if node.a[ord(s[i])-97] is None:
                return 0
            node = node.a[ord(s[i])-97]
        
        # no need to check for end
        return node.count
        
            
            
t = Trie()
t.insert("hello")
t.insert("hello")
t.insert("hello")
t.insert("hillo")
t.insert("hillo")
# t.erase("hello")
# t.erase("hello")
# t.erase("hello")
t.erase("hillo")
# print(t.search("hello"))
print(t.count_startwith("h"))
print(t.count_startwith("hill"))

print(t.count_complete("hello"))
print(t.count_complete("hillo"))


                
                

                    
                
                
        
    
        
        
    


                
            
            
            
        
            
        
