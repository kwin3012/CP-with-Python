from sys import stdin
input = stdin.readline
 
from queue import Queue

def inv(x):
	return pow(x,mod-2,mod)
def nCr(n,r):
	return (f[n]*inv((f[r]*f[n-r])%mod))%mod
 
a = []
n,m = map(int,input().split())
for i in range(n):
    s = input().strip()
    a.append(s)
 
def check(i,j,a):
        b = []
        if i-1>=0 and j>=0:
            if a[i-1][j]=="." or a[i-1][j]=="B":
                b.append(i-1 + j*1000)
        if i>=0 and j-1>=0:
            if a[i][j-1]=="." or a[i][j-1]=="B":
                b.append(i+(j-1)*1000)
        if i+1<len(a) and j>=0:
            if a[i+1][j]=="." or a[i+1][j]=="B":
                b.append(i+1+j*1000)
        if i>=0 and j+1<len(a[0]):
            if a[i][j+1]=="." or a[i][j+1]=="B":
                b.append(i+(j+1)*1000)
        return b
 
d = {}
for i in range(n):
    for j in range(m):
        if a[i][j] == "A":
            source = i+j*1000
        if a[i][j]=="B":
            destination = i+j*1000
        if a[i][j]=="." or a[i][j]=="A":
            b = check(i,j,a)
            d[i+j*1000] = b
 
q = Queue()
visited = [ [0 for i in range(m)] for j in range(n)]
distance = [0]*(1000000)
pred = [-1]*(1000000)
p=0
 
q.put(source)
visited[source%1000][source//1000] = 1
while(q.qsize()>0):
    node = q.get()
    # visited[node%1000][node//1000] = 1
 
    for num in d[node]:
        if visited[num%1000][num//1000] == 0:
            distance[num]=distance[node]+1
            pred[num]=node
            q.put(num)
            visited[num%1000][num//1000] = 1
 
            if num == destination:
                p=1
                break
    if p:
        break
 
if p==0:
    print("NO")
else:
    print("YES")
    print(distance[destination])
 
    curr = destination
    ans = ""
 
    while(pred[curr] != -1):
        bi=curr%1000
        bj=curr//1000
        ai=pred[curr]%1000
        aj=pred[curr]//1000
 
        if bi-ai == 0 and bj-aj==1:
            ans+="R"
        if bi-ai == 0 and bj-aj==-1:
            ans+="L"
        if bi-ai == 1 and bj-aj==0:
            ans+="D"
        if bi-ai== -1 and bj-aj==0:
            ans+="U"
 
        curr = pred[curr]
 
    ans = ans[::-1]
 
    print(ans)