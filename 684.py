import math
f0=0
f1=1
a=2
fib=[]
while a<=90:
    f2=f0+f1
    f0=f1
    f1=f2
    fib.append(f2)
    a=a+1
ans=0
def ksm(a,n):
    res=1
    while n>0:
        if n%2 ==1:
            res=res*a%1000000007
        a=a*a%1000000007
        n=n/2
    return res
def cal(k):
    res=0
    t=k/9
    res=(res+6*(ksm(10,t)+1000000007-1)-9*t)%1000000007
    for b in range(0,k%9):
        res=(res+((b+2)*ksm(10,t)-1)%1000000007)%1000000007
    return res
print(cal(20))
for x in fib:
    ans=(ans+cal(x))%1000000007
print(ans)
    