def facto(n):
    fact=1
    i=1
    while i<=n:
        fact=fact*i
        i=i+1
    print(f"Factorial of {n} is {fact}")
num=int(input("Enter a number="))
facto(num)