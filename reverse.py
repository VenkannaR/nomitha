n=123

def reverse(n):
    rev=0
    while(n>0):
        lastdigit=n%10
        rev=(rev*10)+lastdigit
        n//=10
    print(rev)
a=reverse(n)
    


