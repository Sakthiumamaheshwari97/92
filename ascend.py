dog=int(input())
cat=list(map(int,input().split()))
for i in range(len(cat)-1):
     if(cat[i]>cat[i+1]):
           print(i)
           break
    
        
