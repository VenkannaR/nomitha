import time
L1=[x for x in range(0,1000000)]
sum=20
def get_pairs(li,sum):
    numbers_needed= set()
    pairs={}
    for i in range(0,len(li)):
        exits=li[i] in numbers_needed
        diff=sum-li[i]
        if exits:
            pairs[li[i]]=diff
        else:
            numbers_needed.add(diff)
    print(pairs)

def get_pairs_list(li,sum):
    numbers_needed= []
    pairs={}
    for i in range(0,len(li)):
        exits=li[i] in numbers_needed
        diff=sum-li[i]
        if exits:
            pairs[li[i]]=diff
        else:
            numbers_needed.append(diff)
    print(pairs)
    
start_time=time.time()
get_pairs(L1,sum)
end_time=time.time()
print(end_time-start_time)

#n * n
def add(L1,sum):

    n=len(L1)
    for i in range(0,n):
        for j in range(i+1,n):
            if(L1[i]+L1[j]==sum):
                print(L1[i],L1[j])
start_time=time.time()
get_pairs_list(L1,sum)
end_time=time.time()
print(end_time-start_time)