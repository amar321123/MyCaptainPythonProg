li=[]
num=0
n=int(input("enter the numbr of elements in the list"))
for i in range(0, n): 
    a=int(input())
    li.append(a)
while(num < len(li)): 
    if li[num] >= 0: 
        print(li[num],end = " ")
    num += 1
     
    
        