l1=[9,10,11,12,13,14,20,24,26,29,30,2,5,6,7]
print(("  hehhh  ").strip())
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

# n * n
def find_missing_number(numbers):
    n=len(numbers)

    for i in range(1,n):
        exits=False
        for j in numbers:
            if(i==j):
                exits=True
        if(not exits):
            return i
#n log n
def find_missing_number_by_sort(numbers):
    n=len(numbers)
    numbers.sort()
    for i in range(0,n):
        if(i!=numbers[i]):
            return i
#n
def find_missing_number_by_sum(numbers):
    n=len(numbers)
    return get_sum_of_n_numbers(n)-get_sum_of_numbers(numbers)

def get_sum_of_n_numbers(n):
    sum=0; i=0
    while(i<=n):
        sum+=i
        i+=1
    return sum

def get_sum_of_numbers(numbers):
    sum=0
    for num in numbers:
        sum+=num
    return sum

       
    
        


    



















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

print(find_missing_number_by_sum([5,6,0,8,1,2,3,4]))       

a=swap_binary(l1)
print(a)

