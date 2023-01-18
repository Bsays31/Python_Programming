# Write a function to display fibonacci series upto 10 terms....?

def fibo(x):
    i = 0
    ft = 0
    st = 1
    while x > i:
        print(ft,end=" ")
        nt = ft + st
        ft = st
        st = nt       
        i+=1


nums = int(input("Enter how many terms you want to print :"))
fibo(nums)