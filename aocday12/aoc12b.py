lines=[]
line=input()
while (line!='end'):
    lines.append([line[0],int(line[1:])])
    line=input()
# direc=['N','E','S','W']
movement=[0,0,0,0]
v1=1
v2=10
w1=0
w2=1
currDirec=1
for line in lines:
    if line[0]=='F':
        movement[w1]+=v1*line[1]
        movement[w2]+=v2*line[1]
    if line[0]=='N':
        if w1==0:
            v1+=line[1]
        if w2==0:
            v2+=line[1]
        if w1==2:
            v1-=line[1]
            if v1<0:
                v1*=-1
                w1=0
        if w2==2:
            v2-=line[1]
            if v2<0:
                v2*=-1
                w2=0
    if line[0]=='E':
        if w1==1:
            v1+=line[1]
        if w2==1:
            v2+=line[1]
        if w1==3:
            v1-=line[1]
            if v1<0:
                v1*=-1
                w1=1
        if w2==3:
            v2-=line[1]
            if v2<0:
                v2*=-1
                w2=1
    if line[0]=='S':
        if w1==2:
            v1+=line[1]
        if w2==2:
            v2+=line[1]
        if w1==0:
            v1-=line[1]
            if v1<0:
                v1*=-1
                w1=2
        if w2==0:
            v2-=line[1]
            if v2<0:
                v2*=-1
                w2=2
    if line[0]=='W':
        if w1==3:
            v1+=line[1]
        if w2==3:
            v2+=line[1]
        if w1==1:
            v1-=line[1]
            if v1<0:
                v1*=-1
                w1=3
        if w2==1:
            v2-=line[1]
            if v2<0:
                v2*=-1
                w2=3
    if line[0]=='R':
        w1+=(line[1]/90)
        w1%=4
        w1=int(w1)
        w2+=(line[1]/90)
        w2%=4
        w2=int(w2)
    if line[0]=='L':
        w1-=(line[1]/90)
        if w1<0:
            w1=4+w1
        w1=int(w1)
        w2-=(line[1]/90)
        if w2<0:
            w2=4+w2
        w2=int(w2)
print(abs(movement[0]-movement[2])+abs(movement[1]-movement[3]))