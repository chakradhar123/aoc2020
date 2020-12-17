import numpy as np
import copy
lines=[]
line=input()
while (line!='end'):
    lines.append(line)
    line=input()
grid=[]



grid=np.zeros((4,3,len(lines),len(lines[0])))

for i in range(0,len(lines)):
    for j in range(0,len(lines[0])):
        if lines[i][j]=='#':
            grid[1,1,i,j]=1

gridSides=[]
for i in [-1,0,1]:
    for j in[-1,0,1]:
        for k in [-1,0,1]:
            for l in [-1,0,1]:
                if i!=0 or j !=0 or k!=0 or l!=0:
                    gridSides.append([i,j,k,l])


def check(g,i,j,k,l):
    if i>=0 and j>=0 and k>=0 and l>=0 and i<g.shape[0] and j<g.shape[1] and k<g.shape[2] and l<g.shape[3]:
        return True
    return False
def countHash(g,i,j,k,l):
    count=0
    for item in gridSides:
        if check(g,i+item[0],j+item[1],k+item[2],l+item[3]) and g[i+item[0],j+item[1],k+item[2],l+item[3]]==1:
            count+=1

    return count
grid=np.pad(grid,((1,1),(1,1),(1,1),(1,1)),'constant')
for cycle in range(0,6):
    grid2=copy.deepcopy(grid)
 
        
    for i in range(0,grid.shape[0]):
        for j in range(0,grid.shape[1]):
            for k in range(0,grid.shape[2]):
                for l in range(0,grid.shape[3]):
                    count=countHash(grid,i,j,k,l)
                   
                    
                    if grid[i,j,k,l]==0 and count==3:
                        grid2[i,j,k,l]=1
                    if grid[i,j,k,l]==1 and (count==2 or count==3):
                        grid2[i,j,k,l]=1
                    elif grid[i,j,k,l]==1:
                        grid2[i,j,k,l]=0
                
    grid=grid2
    grid=np.pad(grid,((1,1),(1,1),(1,1),(1,1)),'constant')
    

print(grid.sum())
            
    
   
    