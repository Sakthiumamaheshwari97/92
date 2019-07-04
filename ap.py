a,d,n=map(int,input().split())
current=0
for i in range(0,n):
   current=current+a
   a=a+d
print(current)
    
