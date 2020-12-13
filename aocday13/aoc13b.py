line1=int(input())
line2=input().split(',')

def inv(a, m) : 
      
    m0 = m 
    x0 = 0
    x1 = 1
  
    if (m == 1) : 
        return 0
  
    # Apply extended Euclid Algorithm 
    while (a > 1) : 
        # q is quotient 
        q = a // m 
  
        t = m 
  
        # m is remainder now, process  
        # same as euclid's algo 
        m = a % m 
        a = t 
  
        t = x0 
  
        x0 = x1 - q * x0 
  
        x1 = t 
      
    # Make x1 positive 
    if (x1 < 0) : 
        x1 = x1 + m0 
  
    return x1 
arr=[]

for i in range(0,len(line2)):
    if line2[i]!="x":
        arr.append([int(line2[i]),(len(line2)-i)%int(line2[i])])

prod=1
pp=[]

for item in arr:
    prod*=item[0]

for item in arr:
    pp.append(int(prod/item[0]))
inver=[]

for i in range(0,len(arr)):
    inver.append(inv(pp[i],arr[i][0]))
s=0
for i in range(0,len(arr)):
    s+=(arr[i][1]*pp[i]*inver[i])
print((s%prod)-len(line2))



