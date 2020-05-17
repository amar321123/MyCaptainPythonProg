n=input("enter the file name with extension")
li=list(n.split("."))
a=li[-1]
d={"py":"python","pdf":"portable document format","js":"javascript"}
print(d[a])