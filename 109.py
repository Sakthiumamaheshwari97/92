m,n=map(int,input().split())
list=input().split()
lg=[]
for i in list:
  if (int(i)%2!=0):
    lg.append(i)
print(lg[n-1])
