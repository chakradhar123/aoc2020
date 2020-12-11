import copy
lines=[]
line=input()
while (line!='end'):
    lines.append(line)
    line=input()

w=len(lines[0])
h=len(lines)
totalseats=0
for i in range(h):
    lines[i]=list(lines[i])
for i in range(h):
    for j in range(w):
        if lines[i][j]=='L':
            totalseats+=1

borders=[]
for i in range(h):
    borders.append([])
def findBorers(i,j):
    border=[[-1,-1],[-1,-1],[-1,-1],[-1,-1],[-1,-1],[-1,-1],[-1,-1],[-1,-1]]
    for p in range(j+1,len(lines[0])):
        if lines[i][p]!='.':
            border[0]=[i,p]
            break
    for p in range(i+1,len(lines)):
        if lines[p][j]!='.':
            border[1]=[p,j]
            break
    for p in range(-1*(j-1),1):
        if lines[i][-1*p]!='.':
            border[2]=[i,-1*p]
            break
    for p in range(-1*(i-1),1):
        if lines[-1*p][j]!='.':
            border[3]=[-1*p,j]
            break
    p=i-1
    q=j-1
    while p>=0 and q>=0:
        if lines[p][q]!='.':
            border[4]=[p,q]
            break
        p-=1
        q-=1
    p=i+1
    q=j-1
    while p<len(lines) and q>=0:
        if lines[p][q]!='.':
            border[5]=[p,q]
            break
        p+=1
        q-=1
    p=i-1
    q=j+1
    while p>=0 and q<len(lines[0]):
        if lines[p][q]!='.':
            border[6]=[p,q]
            break
        p-=1
        q+=1
    
    p=i+1
    q=j+1
    while p<len(lines) and q<len(lines[0]):
        if lines[p][q]!='.':
            border[7]=[p,q]
            break
        p+=1
        q+=1
    borders[i].append(border)

for i in range(h):
    for j in range(w):
        findBorers(i,j)

def countAdjL(arr,i,j):
    count=0
    for p in range(0,8):
        if borders[i][j][p][0]!=-1 and borders[i][j][p][1]!=-1 and arr[borders[i][j][p][0]][borders[i][j][p][1]]=='L':
            count+=1
        
    return count
def checkAdjHash(arr,i,j):
    for p in range(0,8):
        if borders[i][j][p][0]!=-1 and borders[i][j][p][1]!=-1 and arr[borders[i][j][p][0]][borders[i][j][p][1]]=='#':
            return True
    return False
prev=copy.deepcopy(lines)
curr=copy.deepcopy(prev)
ans=0
while(totalseats>0):
    for i in range(h):
        for j in range(w):
            if prev[i][j]=='L':
                if countAdjL(prev,i,j)<5:
                    curr[i][j]='#'
                    totalseats-=1
                    ans+=1
    
    for i in range(h):
        for j in range(w):
            if curr[i][j]=='L' and (checkAdjHash(curr,i,j)):
                curr[i][j]='P'
                totalseats-=1
    prev=copy.deepcopy(curr)
print(ans)