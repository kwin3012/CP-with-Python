class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
class minheap:
    def __init__(self):
        self.a = []
        
    def getsize(self):
        return len(self.a)
    
    def insert(self,node):
        self.a.append(node)
        ci = len(self.a) - 1
        pi = (ci-1)//2
        while(pi>=0):
            if self.a[pi].val>self.a[ci].val:
                self.a[pi],self.a[ci] = self.a[ci],self.a[pi]
            else:
                break
            ci = pi
            pi = (ci-1)//2
        
    def remove(self):
        if len(self.a) == 0:
            return "Empty"
        
        self.a[0],self.a[-1] = self.a[-1],self.a[0] # exchange
        ele = self.a.pop()
            
        te = len(self.a)
        pi = 0
        while(1):
            if 2*pi+2<te:
                if self.a[2*pi+1].val <= self.a[2*pi+2].val:
                    if self.a[pi].val<self.a[2*pi+1].val:
                        break
                    else:
                        self.a[pi],self.a[2*pi+1] = self.a[2*pi+1],self.a[pi]
                        pi = 2*pi+1
                else:
                    if self.a[pi].val < self.a[2*pi+2].val:
                        break
                    else:
                        self.a[pi],self.a[2*pi+2] = self.a[2*pi+2],self.a[pi]
                        pi = 2*pi+2
                        
            elif 2*pi + 1<te:
                if self.a[pi].val<self.a[2*pi+1].val:
                    break
                else:
                    self.a[pi],self.a[2*pi+1] = self.a[2*pi+1],self.a[pi]
                    pi = 2*pi+1
            else:
                break
                
        return ele

#----------------------------Max Heap-----------------------------------#

class Node:
    def __init__(self, val=-1, index=-1):
        self.val = val
        self.index = index

class maxheap:
    def __init__(self):
        self.a = []
        
    def getsize(self):
        return len(self.a)
    
    def insert(self,node):
        self.a.append(node)
        ci = len(self.a) - 1
        pi = (ci-1)//2
        while(pi>=0):
            if self.a[pi].val<self.a[ci].val:
                self.a[pi],self.a[ci] = self.a[ci],self.a[pi]
            else:
                break
            ci = pi
            pi = (ci-1)//2
        
    def remove(self):
        if len(self.a) == 0:
            return "Empty"
          
        self.a[0],self.a[-1] = self.a[-1],self.a[0] # exchange
        ele = self.a.pop()
            
        te = len(self.a)
        pi = 0
        while(1):
            if 2*pi+2<te:
                if self.a[2*pi+1].val >= self.a[2*pi+2].val:
                    if self.a[pi].val>=self.a[2*pi+1].val:
                        break
                    else:
                        self.a[pi],self.a[2*pi+1] = self.a[2*pi+1],self.a[pi]
                        pi = 2*pi+1
                else:
                    if self.a[pi].val >= self.a[2*pi+2].val:
                        break
                    else:
                        self.a[pi],self.a[2*pi+2] = self.a[2*pi+2],self.a[pi]
                        pi = 2*pi+2
                        
            elif 2*pi + 1<te:
                if self.a[pi].val>=self.a[2*pi+1].val:
                    break
                else:
                    self.a[pi],self.a[2*pi+1] = self.a[2*pi+1],self.a[pi]
                    pi = 2*pi+1
            else:
                break
                
        return ele