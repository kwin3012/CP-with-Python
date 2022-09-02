from sys import stdin
input = stdin.readline

t = int(input())

def build(node,l,r):
    if l==r:
        tree[node] = a[l]
        return
    
    m = (l+r)//2

    build(2*node,l,m)
    build(2*node+1,m+1,r)

    tree[node] = tree[2*node] + tree[2*node+1]

def sum_segment(ri):
    s = 0
    l=0
    r=n-1
    node = 1
    while(ri!=r):
        m = (l+r)//2
        if l<=ri<=m:
            node = 2*node
            r = m
        else:
            s = s + tree[2*node]
            node = 2*node+1
            l=m+1
    s = s + tree[node]
    return s
        

for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    # q = int(input())
    b = []
    # for i in range(q):
    #     u,x,y = map(int,input().split())
    #     b.append([u,x,y])

    tree = [-1]*(4*n) # tree starts from index 1 to 2*n-1
    build(1,0,n-1) 

    print(tree)

    # for i in range(q):
    #     if b[i][0]==1:
    #         x = b[i][1]           # position at which we want to update val
    #         temp = a[x]           # stores the value of position that needs to be updated
    #         val = b[i][2]         # value which needs to be updated at x position
    #         l=0                   # start 
    #         r=n-1                 # end
    #         node = 1              # index to update subsequent tree values
        
    #         while(l!=r):
    #             tree[node] += (val-temp)
    #             m = (l+r)//2
    #             if l<=x<=m:
    #                 r=m
    #                 node = 2*node
    #             else:
    #                 l=m+1
    #                 node = 2*node+1
    #         a[l]=val
    #         tree[node]+=(val-temp)

    #         print(a)
    #         print(tree)
    #     else:
    #         li = b[i][1]
    #         ri = b[i][2]

    #         s2 = sum_segment(ri)
    #         print(s2)
    #         if li == 0:
    #             s1 = 0
    #         else:
    #             s1 = sum_segment(li-1)
    #         s = s2-s1

    #         print(s,s2,s1)
            
            



