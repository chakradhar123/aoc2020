lines=[]
line=input()
while (line!='end'):
    lines.append([line[0],int(line[1:])])
    line=input()
# direc=['N','E','S','W']
movement=[0,0,0,0]
currDirec=1
for line in lines:
    if line[0]=='F':
        movement[currDirec]+=line[1]
    if line[0]=='N':
        movement[0]+=line[1]
    if line[0]=='E':
        movement[1]+=line[1]
    if line[0]=='S':
        movement[2]+=line[1]
    if line[0]=='W':
        movement[3]+=line[1]
    if line[0]=='R':
        currDirec+=(line[1]/90)
        currDirec%=4
        currDirec=int(currDirec)
    if line[0]=='L':
        currDirec-=(line[1]/90)
        if currDirec<0:
            currDirec=4+currDirec
        currDirec=int(currDirec)
print(abs(movement[0]-movement[2])+abs(movement[1]-movement[3]))