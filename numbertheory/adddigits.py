#https://leetcode.com/problems/add-digits/
while(True):
    n=int(input("Enter the number: "))
    if(n==0):
        print(0)
    else:
        print((n-1)%9 +1)