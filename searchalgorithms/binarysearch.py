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