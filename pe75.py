import time
t1=time.time()
count=0
for i in range(1,1500001):
 count_tem=0
 
 for j in range(i):
  for k in range(j+1,i):
   if not j+k>i:
    continue
   if (i)**2==(j**2+k**2):
    count_tem+=1
    m=j
    n=k
 if count_tem==1:
  if i+m+n>1500000:
   print(count)
   print("total time:" ,(time.time()-t1))
   exit(0)
  print(i,m,n)
  count+=1
  #print(count)
