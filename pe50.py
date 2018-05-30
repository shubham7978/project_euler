from isprime import isprime
 
if __name__=='__main__':
	list=[]
	sum=0
	for i in range(2, 99999):
		if isprime(i)==1:
			print(i)
			list.append(i)
			sum+=i
			if(sum>1000000):
			  print(psum)
			  print(len(list))
			  print(lenlist)
			  print(rsum)
			  exit(0)
			rsum=sum
			if isprime(sum)==1:
				psum=sum
				lenlist=len(list)
