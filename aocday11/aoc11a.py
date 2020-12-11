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

def countAdjL(arr,i,j):
    count=0
    if i-1>=0 and arr[i-1][j]=='L':
        count+=1
    if j-1>=0 and arr[i][j-1]=='L':
        count+=1
    if j-1>=0 and i-1>=0 and arr[i-1][j-1]=='L':
        count+=1
    if i+1<len(arr) and arr[i+1][j]=='L':
        count+=1
    if j+1<len(arr[0]) and arr[i][j+1]=='L':
        count+=1
    if i+1<len(arr) and j+1<len(arr[0]) and arr[i+1][j+1]=='L':
        count+=1
    if i-1>=0 and j+1<len(arr[0]) and arr[i-1][j+1]=='L':
        count+=1
    if i+1<len(arr) and j-1>=0 and arr[i+1][j-1]=='L':
        count+=1
    return count
def checkAdjHash(arr,i,j):
    if i-1>=0 and arr[i-1][j]=='#':
        return True
    if j-1>=0 and arr[i][j-1]=='#':
        return True
    if j-1>=0 and i-1>=0 and arr[i-1][j-1]=='#':
        return True
    if i+1<len(arr) and arr[i+1][j]=='#':
        return True
    if j+1<len(arr[0]) and arr[i][j+1]=='#':
        return True
    if i+1<len(arr) and j+1<len(arr[0]) and arr[i+1][j+1]=='#':
        return True
    if i-1>=0 and j+1<len(arr[0]) and arr[i-1][j+1]=='#':
        return True
    if i+1<len(arr) and j-1>=0 and arr[i+1][j-1]=='#':
        return True
    return False
prev=copy.deepcopy(lines)
curr=copy.deepcopy(prev)
ans=0
while(totalseats>0):
    for i in range(h):
        for j in range(w):
            if prev[i][j]=='L':
                if countAdjL(prev,i,j)<4:
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