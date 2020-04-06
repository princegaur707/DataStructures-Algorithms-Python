# T.C O(n^2)
''' Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements
if they are in wrong order. '''
def bubblesort(arr,n):
    for i in range(0,n-1):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr

arr = [64, 34, 25, 12, 22, 11, 90] 
print(bubblesort(arr,len(arr)))
