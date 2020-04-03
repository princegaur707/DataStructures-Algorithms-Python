def xor1ton(n):
    if n%4==0:
        return n
    if n%4==1:
        return 1
    if n%4==2:
        return n+1
    else:
        return 0
while True:
    try:
        n=int(input("Enter number:    "))
        print(xor1ton(n))
    except:
        print("Invalid input!")
        break
