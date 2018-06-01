import math
def ispalindrome(n):
 s=list(str(n))
 hl=math.floor(len(s)/2)
 for j in range(hl):
  if not  s[j]==s[-1-j]:
   return 0 
 return 1

fsum=0
for i in range (2,100000000):
 if ispalindrome(i):
  #print(i)
  for k in range(1,math.floor(i**(0.5))):
   l=k
   sum=0
   while sum<i:
    sum+=l**2
    l+=1
   if sum==i:
     fsum+=i
     print(i)
     break
print(fsum)


