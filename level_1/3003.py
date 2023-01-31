pices = list(map(int, input().split()))
bk = [1,1,2,2,2,8]
sum=[]

for i in range(len(bk)):
    a = bk[i] - pices[i]
    sum.append(a)

print(' '.join(map(str,sum)))