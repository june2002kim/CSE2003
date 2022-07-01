n=int(input("Enter N (0 < N < 10) : "))
x=''
if n<=0 or n>=10:
    print("ERROR: N must be 0 < N < 10.")
    
else:
    if n%2!=0:
        for i in range(1, n+1):
            for j in range(1, i+1):
                x+=str(j)
            print(x)
            x=''
        for i in range(n-1, 0, -1):
            for j in range(1, i+1):
                x+=str(j)
            print(x)
            x=''
    else:
        for i in range(1, n+1):
            for j in range(1, i+1):
                x+=str(j)
            print(x)
            x=''
        for i in range(n, 0, -1):
            for j in range(1, i+1):
                x+=str(j)
            print(x)
            x=''
