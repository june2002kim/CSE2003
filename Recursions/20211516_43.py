#Fibonacci
def Fib(n):
    if n==0 or n==1:
        return n
    else:
        return Fib(n-1)+Fib(n-2)

n=int(input("Input N: "))
print(f"First {n} Fibonacci numbers:\n")

cnt=0

for i in range(n):
    print(f"{Fib(i):>9}", end="")

    cnt+=1
    if cnt%5==0:
        print(",\n")
    else:
        print(",", end="")
