import bisect

ls=[1,2,3,4,5,6,7,8,9,10]
bisect.insort(ls,4)  #returns sorted list after inserting number (inserts according to bisect_right rule)
print(ls)
bisect.insort_left(ls,9) #insert according to bisect_left and returns this edited list
print(ls)