s=[int(x) for x in list(input())]
moves=0
i=0
n=len(s)
m=max(s)
while moves!=100:
    curr=s[i]
    temparr=[s[(i+1)%n],s[(i+2)%n],s[(i+3)%n]]
   
    p=i
    s.pop((p+1)%len(s))
    p=s.index(curr)
    s.pop((p+1)%len(s))
    p=s.index(curr)
    s.pop((p+1)%len(s))
   
    tempcurr=curr
    while(True):
        curr-=1
        if(curr==0):
            curr=m
        if curr in s and curr not in temparr:
            pos=s.index(curr)
            s.insert((pos+1),temparr[2])
            pos=s.index(curr)
            s.insert((pos+1),temparr[1])
            pos=s.index(curr)
            s.insert((pos+1),temparr[0])
            break
    
    i=(s.index(tempcurr)+1)%len(s)



    moves+=1
pos1=s.index(1)
print(''.join([str(x) for x in s[pos1+1:]])+''.join([str(x) for x in s[:pos1]]))