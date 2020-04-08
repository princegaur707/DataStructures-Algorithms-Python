def groupana(arr):
    a=[[]]  
    l=len(arr)
    for i in range(l):
        arr[i]=list(arr[i])
        if(arr[i].sort not in a):
            a.append(str(arr[i]))
    return a
while True:
    print(groupana(["eat", "tea", "tan", "ate", "nat", "bat"]))
    
