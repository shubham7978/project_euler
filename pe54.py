#!/usr/bin/python
if __name__=='__main__':
	fo = open("poker54.txt","r")
	str1=fo.read()
	a=str.split("str1", "\n")
	sp1=0
	sp2=0
	for i in range(0, len(a)):
	 p1[i]=a[i][0:14]
	 p2[i]=a[i][15:]
	 if (score(p1[i])>score(p2[i])) :
	  sp1+=1
	 else:
	  sp2+=1 
	print("player1 score is %d ", % sp1)
	exit(0)

def score(txt):
 if royal_flush(txt):
  scr+=100
 if straight_flush(txt):
  scr+
