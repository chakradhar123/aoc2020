import numpy as np
lines=[]
line=input()
lineDict={}
integers=[]
while (line!='end'):
    if line=='':
        lineDict[int(lines[0][5:-1])]=np.array([list(item) for item in lines[1:]])
        integers.append(int(lines[0][5:-1]))
        lines=[]
    else:
        lines.append(line)
    line=input()
lineDict[int(lines[0][5:-1])]=np.array([list(item) for item in lines[1:]])
integers.append(int(lines[0][5:-1]))
lineDict2={}

for key,value in lineDict.items():
    li=[]
    li.append(value)
    li.append(np.rot90(value))
    li.append(np.rot90(value,2))
    li.append(np.rot90(value,3))
    li.append(value[::-1])
    li.append(np.rot90(value[::-1]))
    li.append(np.rot90(value[::-1],2))
    li.append(np.rot90(value[::-1],3))
    li.append(np.flip(value,1))
    li.append(np.rot90(np.flip(value,1)))
    li.append(np.rot90(np.flip(value,1),2))
    li.append(np.rot90(np.flip(value,1),3))


    
    lineDict2[key]=li
    


class Tile:
    id=0
    tiles=[]
    marked=None
    up=None
    down=None
    left=None
    right=None
    def __init__(self,id,li):
        self.id=id
        self.tiles=li


for i in range(0,len(integers)):
    lineDict2[integers[i]]=Tile(integers[i],lineDict2[integers[i]])


queue=[]

queue.append(integers[-1])
visited=set()

def checkdu(id1,id2,pos1):
    if lineDict2[id2].marked!=None:
        if np.array_equal(lineDict2[id1].tiles[pos1][-1,:],lineDict2[id2].tiles[lineDict2[id2].marked][0,:]) :
            lineDict2[id1].down=id2
            lineDict2[id2].up=id1
    else:
        for i in range(0,12):
            if np.array_equal(lineDict2[id1].tiles[pos1][-1,:],lineDict2[id2].tiles[i][0,:]) :
                lineDict2[id1].down=id2
                lineDict2[id2].up=id1
                lineDict2[id2].marked=i
                return
def checkud(id1,id2,pos1):
    if lineDict2[id2].marked!=None:
        if np.array_equal(lineDict2[id1].tiles[pos1][0,:],lineDict2[id2].tiles[lineDict2[id2].marked][-1,:]) :
            lineDict2[id1].up=id2
            lineDict2[id2].down=id1
    else:
        for i in range(0,12):
            if np.array_equal(lineDict2[id1].tiles[pos1][0,:],lineDict2[id2].tiles[i][-1,:]) :
                lineDict2[id1].up=id2
                lineDict2[id2].down=id1
                lineDict2[id2].marked=i
                return
def checklr(id1,id2,pos1):
    if lineDict2[id2].marked!=None:
        if np.array_equal(lineDict2[id1].tiles[pos1][:,0],lineDict2[id2].tiles[lineDict2[id2].marked][:,-1]) :
            lineDict2[id1].left=id2
            lineDict2[id2].right=id1
    else:
        for i in range(0,12):
            if np.array_equal(lineDict2[id1].tiles[pos1][:,0],lineDict2[id2].tiles[i][:,-1]) :
                lineDict2[id1].left=id2
                lineDict2[id2].right=id1
                lineDict2[id2].marked=i
                return

def checkrl(id1,id2,pos1):
    if lineDict2[id2].marked!=None:
        if np.array_equal(lineDict2[id1].tiles[pos1][:-1],lineDict2[id2].tiles[lineDict2[id2].marked][:,0]) :
            lineDict2[id1].right=id2
            lineDict2[id2].left=id1
    else:
        for i in range(0,12):
            if np.array_equal(lineDict2[id1].tiles[pos1][:,-1],lineDict2[id2].tiles[i][:,0]) :
                lineDict2[id1].right=id2
                lineDict2[id2].left=id1
                lineDict2[id2].marked=i
                return
def findEdges(id):

    if lineDict2[id].marked==None:
        
        lineDict2[id].marked=0  
        for integer in integers:
            if integer not in visited:
                if lineDict2[id].right==None:
                    checkrl(id,integer,0)
                if lineDict2[id].left==None:
                    checklr(id,integer,0)    
                if lineDict2[id].up==None:
                    checkud(id,integer,0)
                if lineDict2[id].down==None:
                    checkdu(id,integer,0)
    else:
        for integer in integers:
            if integer not in visited:
                if lineDict2[id].right==None:
                    checkrl(id,integer,lineDict2[id].marked)
                if lineDict2[id].left==None:
                    checklr(id,integer,lineDict2[id].marked)    
                if lineDict2[id].up==None:
                    checkud(id,integer,lineDict2[id].marked)
                if lineDict2[id].down==None:
                    checkdu(id,integer,lineDict2[id].marked)
    

while(len(queue)!=0):
    findEdges(queue[0])
    id=queue[0]
    visited.add(queue[0])
    queue.pop(0)
   
    if lineDict2[id].right!=None:
        if lineDict2[id].right not in queue and lineDict2[id].right not in visited:
            queue.append(lineDict2[id].right)
    if lineDict2[id].left!=None:
        if lineDict2[id].left not in queue and lineDict2[id].left not in visited:
            queue.append(lineDict2[id].left)
    if lineDict2[id].up!=None:
        if lineDict2[id].up not in queue and lineDict2[id].up not in visited:
            queue.append(lineDict2[id].up)
    if lineDict2[id].down!=None:
        if lineDict2[id].down not in queue and lineDict2[id].down not in visited:
            queue.append(lineDict2[id].down)
ans=1
for integer in integers:
    count=0
    if lineDict2[integer].left!=None:
        count+=1
    if lineDict2[integer].right!=None:
        count+=1
    if lineDict2[integer].up!=None:
        count+=1
    if lineDict2[integer].down!=None:
        count+=1
    if count==2:
        ans*=integer
    
    
print(ans)
