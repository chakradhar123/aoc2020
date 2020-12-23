import copy
s=[int(x) for x in list(input())]
moves=0


m=max(s)
mindex=s.index(m)

start=s[0]


i=s.index(start)
cups=1000000
for j in range(m+1,cups+1):
    s.append(j)
n=len(s)



class Node:
    next=None
    data=None
    def __init__(self,n):
        self.data=n

head=Node(s[0])

hashMap=copy.deepcopy(s)
hashMap.append(0)
hashMap[s[0]]=head
curr=head
for i in range(1,len(s)):
    curr.next=Node(s[i])
    curr=curr.next
    hashMap[s[i]]=curr

curr.next=hashMap[s[0]];
  

curr=hashMap[start]
total=10000000
while moves!=total:
    temp1=curr.next.data
    temp2=curr.next.next.data
    temp3=curr.next.next.next.data
    
    currData=curr.data
    while(True):
        currData-=1
        if currData==0:
            currData=cups
        if currData!=temp1 and currData!=temp2 and currData!=temp3:
           
            curr.next=hashMap[temp3].next
            hashMap[temp3].next=hashMap[currData].next
            hashMap[currData].next=hashMap[temp1]
            break
    # print(moves)
    curr=curr.next
    



    moves+=1



print(hashMap[1].next.data*hashMap[1].next.next.data)