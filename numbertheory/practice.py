test=int(input())
array=[]
for i in range(test):
    
    n,t = map(int,input().split())

    v=list(map(int,input().split()))
    #v = [999, 999, 999] 
    s=sorted(v)
    #t=300
    sum=0
    ans=[]
    for i in range(len(s)):
        sum+=s[i]
        if sum<=t:
            ans.append(sum)
        else:
            break    

    array.append(len(ans))  
#print (array)      
    #print (len(ans))
for i in range(test):
    #print (i+1)
    print (f"Case #{i+1}: {array[i]}")
# t=int(input())
# array=[]
# while t>0:
#     n,b=map(int,input().split())
#     arr = list(map(int,input().split()))[:n] 
#     len(arr)
#     h=0
#     i=0
#     arr.sort()
#     while arr[i]<=b:
#         h+=1
#         b-=arr[i]
#         if(i<n):
#             i+=1
#         else:
#             break
#     array.append(h) 
#     t-=1
# for i in range(t):
#     print (f"Case #{i+1}: {array[i]}")
# t=int(input())
# while t:
#     n,b=map(int,input().split())
#     arr = list(map(int,input().split()))[:n] 
#     len(arr)
#     h=0
#     i=0
#     arr.sort()
#     while arr[i]<=b:
#         h+=1
#         b-=arr[i]
#         if(i<n):
#             i+=1
#         else:
#             break
#     print(h) 
#     t-=1    