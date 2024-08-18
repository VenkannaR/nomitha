l1=[9,10,11,12,13,14,20,24,26,29,30,2,5,6,7]
def swap_binary(numbers):
    n=len(numbers)
    left=0
    right=n-1
    while(left<=right):
        mid=(left+right)//2
        if(numbers[mid]<numbers[mid-1]):
            break
        elif(numbers[mid]>numbers[left]):
            left=mid+1
        elif(numbers[mid]<numbers[right]):
            right=mid-1
    return min(mid+1,n-(mid+1))




















def swap2(numbers):
    n=len(numbers)
    start=0
    next=1
    while(numbers[start]<numbers[next]):
        start=next
        next+=1
    return min(next,n-next)

def swap(numbers):
    n=len(numbers)
    left=0
    right=n-1
    while(numbers[left]>numbers[right]):
        right-=1
    return min(right+1,len(numbers)-(right+1))


            

a=swap_binary(l1)
print(a)

