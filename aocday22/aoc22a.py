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

while (len(lines1)!=0 and len(lines2)!=0):
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

winner=[]
if(len(lines1)!=0):
    winner=lines1
else:
    winner=lines2
size=len(winner)
ans=0
for i in range(0,len(winner)):
    ans=ans+winner[i]*size
    size-=1
print(ans)
