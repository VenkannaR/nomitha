def fibonacci(n):
    i=0
    j=1
    print(i)
    print(j)
    for iter in range(0,n+1):
        temp=i+j
        if (temp > n):
            break
        print(temp)
        i,j = j, temp
def fib_rec(n,cache):
   if n in cache:
       return cache[n]
   
   if n<=0:
       return 0
   if n==1:
       return 1
   if n==2:
       return 1
   r= fib_rec(n-1,cache)+fib_rec(n-2,cache)
   cache[n]=r
   return r



a=fib_rec(100,{})
print(a)

        



    