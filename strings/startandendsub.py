#https://www.codechef.com/problems/CSUB

t=int(input())
while t:
    n=int(input())
    str1=input()
    n=str1.count('1')
    print(n*(n+1)//2)
    t-=1