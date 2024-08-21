# n=int(input("enter any number:"))
# for i in range(1,n+1):
#     print(i)


# num=int(input("enter any number:"))
# def rec(num):
#     start=1
#     for i in range(start,num+1):
#         print(i)

   
# a=rec(num)

def print_number(num):
    if (num<=100):
        print(num)
        print_number(num+1)
    else:
        return
    print("exiting function n value "+str(num))
print_number(1)

# 1 1 2 3 5 8 13
# upper limit = 100
# lower limit = 1
