from collections import Counter
n=input("enter the string")
fq=Counter(n)
for i,j in fq.items():
    print(i,j,sep="=")
