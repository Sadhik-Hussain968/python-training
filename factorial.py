'''def fact(n):
    f=1 
    for i in range(1,n+1):
        f*=i
    print(f)
fact(5)'''
#recursion
def facti(n):
    if n==0 or n==1:
       return n 
    return n*facti(n-1)
print(facti(6))

    