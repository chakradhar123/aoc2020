import copy
lines1=[]
lines2=[]
flag=1
line=input()
while (line!='end'):
    if(line=="Player 2:"):
        flag=0
    if line!="" and line!="Player 2:" and line!="Player 1:":

        if flag:
            lines1.append(int(line))
        else:
            lines2.append(int(line))
    
    line=input()

def RecursiveCombat(lines1,lines2,recursive):
   
    seen=set()
    
    
    while (len(lines1)!=0 and len(lines2)!=0):
        state=(tuple(lines1),tuple(lines2))
        if (state in seen):
            return 1
        seen.add(state)

        if len(lines1)-1>=lines1[0] and len(lines2)-1>=lines2[0]:
            temp1=copy.deepcopy(lines1)
            temp2=copy.deepcopy(lines2)
            win=RecursiveCombat(temp1[1:1+lines1[0]],temp2[1:1+lines2[0]],True)
            if(win==1):
                lines1.append(lines1[0])
                lines1.append(lines2[0])
                lines1.pop(0)
                lines2.pop(0)
            else:
                lines2.append(lines2[0])
                lines2.append(lines1[0])
                lines1.pop(0)
                lines2.pop(0)
            continue
        if(lines1[0]>lines2[0]):
            lines1.append(lines1[0])
            lines1.append(lines2[0])
            lines1.pop(0)
            lines2.pop(0)
        else:
            lines2.append(lines2[0])
            lines2.append(lines1[0])
            lines1.pop(0)
            lines2.pop(0)
    
   
    if(len(lines2))==0:
        if (not recursive):
            return lines1
        return 1
    if(len(lines1))==0:
        if (not recursive):
            return lines2
        return 2
        



winner=RecursiveCombat(lines1,lines2,False)

size=len(winner)
ans=0
for i in range(0,len(winner)):
    ans=ans+winner[i]*size
    size-=1
print(ans)

