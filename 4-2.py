'''
对任意各位数字不相同的4位数，使用各位数字能组成的最大数减去能组成的最小数，
对得到的差重复这个操作，最终会得到的数字是什么？验证猜想。
'''
x=list(map(int,input()))
print(x)
def memo(x):
    x_1=sorted(x)#升序
    x_2=sorted(x,reverse=True)#降序
    res=(x_2[0]*1000+x_2[1]*100+x_2[2]*10+x_2[3])\
          -\
          (x_1[0]*1000+x_1[1]*100+x_1[2]*10+x_1[3])
    res=list(map(int,str(res)))
    return res
while True:
    print(memo(x))
    x=memo(x)