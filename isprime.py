#class isprime :
import math, sys
def isprime(a):
	for i in range(2, (1+math.ceil(a/2))):
		if (a%i==0) :
			return 0
	return 1

if __name__=='__main__':
	num=sys.argv[1]
	num=int(num)
	print(num)
	print(isprime(num))
#print(isprime(11))
			
	
