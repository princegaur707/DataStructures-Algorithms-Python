def bintodec(b):
    d=0
    k=0
    while b:
        d+=2**k*(b%10)
        k+=1
        b//=10
    return d
while True:
    try:
        b=int(input("Enter number:   "))
        print(bintodec(b))
    except:
        print("Invalid input!")
        break