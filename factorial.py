n=5


def factorial_rec(n):
    if(n==0):
        return 1
    else:
        return n*factorial(n-1)
def sum(n):
    sum=0
    for i in range(n):
        sum+=i
    return sum
def factorial(n):
    factorial=1
    for i in range(1,n+1):
        factorial*=i
    return factorial
a=factorial_rec(n)
print(a)



