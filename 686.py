import math
def check(a):
    log2=math.log(2)/math.log(10)
    logx=a*log2
    x=logx-math.floor(logx)
    y=pow(10,x)-1.23
    if 0<= y and y<0.01:
        return 1
    return 0
b=1
log2=math.log(2)/math.log(10)
a=90
while a<100000000000000:
    if check(a+196)==1:
        b=b+1
        a=a+196
        ##print(b,a)
    elif check(a+289)==1:
        b=b+1
        a=a+289
        ##print(b,a)
    elif check(a+485)==1:
        b=b+1
        a=a+485
        ##print(b,a)
    if b%1000==0 or b==678910:
        print(b,a)
        if b==678910:
            break
        #(678910, 193060223)