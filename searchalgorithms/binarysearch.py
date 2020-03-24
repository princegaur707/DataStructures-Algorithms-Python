''' Key Points
Binary Search is only applied on sorted array
Time Complexity O(logn)
T(n) = T(n/2) + 1
'''
def binSearch(arr,key,left,right):
    if left > right:
        return -1
    mid = (left + right) // 2
    if arr[mid]==key:
        return mid
    elif arr[mid] < key:
        return binSearch(arr,key,mid+1,right)
    else:
        return binSearch(arr,key,left,mid-1)
t=int(input())
while t:
    arr = list(map(int,input().split()))
    key = int(input())
    print(binSearch(arr,key,0,len(arr)-1))
    t=t-1
    