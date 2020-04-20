#https://www.geeksforgeeks.org/bisect-algorithm-functions-in-python/
import bisect
#bisect return the position to insert any element so that resultant list remain sorted
ls=[1,2,3,4,4,6,7,8,9]
print(bisect.bisect(ls,4,0,len(ls))) #bisect(list, num, beg, end) : In case of already present element return rightmost position
print(bisect.bisect_left(ls,4)) #bisect_left(list,num,beg,end): In case of already present element return leftmost position
print(bisect.bisect_right(ls,4)) #same as normal bisect function if beg and end are not given it consider it from 0 to length of list

