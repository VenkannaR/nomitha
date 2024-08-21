L1=L1=[x for x in range(0,1000000)]
def sort(L1):
    n=len(L1)-1
    for i in range(n,-1,-1):
        for j in range(i-1,-1,-1):
            if(L1[i]<L1[j]):
                temp=L1[i]
                L1[i]=L1[j]
                L1[j]=temp
    print(L1)


# def sort(L1):
#     n=len(L1)
#     for i in range(0,n):
#         for j in range(i+1,n):
#             if(L1[i]>L1[j]):
#                 L[i]L[j]=L[j]L[i]
#     print(L1)





a=sort(L1)
