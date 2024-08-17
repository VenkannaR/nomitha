l1=[58,10,20,30,40,52,53,54,55,56,57]
#Linear Search
def linear_search(numbers,number):
    for i in numbers:
        if(i==number):
            return True
    return False

# Binary Search
def binary_search(numbers,number):
    n=len(numbers)
    left=0
    right=n-1
    while(left<=right):
        mid=(left+right)//2
        if(numbers[mid]==number):
            return True
        elif(numbers[mid]>number):
            right=mid-1
        elif(numbers[mid]<number):
            left=mid+1
    return False

  
a=binary_search(l1,2)
print(a)
print(binary_search(l1,20))