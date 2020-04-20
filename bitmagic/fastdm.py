# x >> y , x divide by 2^y
# x << y , x multiply by 2^y

while True:
    try:
        n = int(input("Enter number:   "))
        print(n>>1,n<<1)
    except:
        print("Invalid input!")
        break