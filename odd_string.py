def odd_string(n):
    odd='a'
    odd= (n-1)*odd
    if(n%2==0):
        return odd+"b"
    else:
        return odd+"a"
a=odd_string(5)
print(a)
