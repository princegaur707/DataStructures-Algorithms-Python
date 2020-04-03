def pow(x,n):
    if n==0:
        return 1
    if n==1:
        return x
    if n%2==0:
        return pow(x*x,n/2)
    else:
        return x*pow(x*x,(n-1)/2)

while True:
    try:
        x,n=map(int,input("Enter x and n:      ").split())
        print(pow(x,n))
    except:
        print("Invalid input!")
        break