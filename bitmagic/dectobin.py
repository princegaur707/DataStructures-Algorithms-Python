def dectobin(n):
    b=0
    k=0
    while n:
        b+=10**k*(n%2)
        k+=1
        n=n//2
    return b
while True:
    try:
        n=int(input("Enter number:  "))
        print(dectobin(n))
    except:
        print("Invalid input!")
        break