h,m = map(int, input().split())
c = int(input())

# if h>0 and m+c>60 :
#     print()
if m+c <60:
    print(h, m+c)
elif h == 23 and m+c > 60:
    m = (m+c)-60
    h = ((m+c)//60)
    print(h, m)
    
    
else :
    print(h+1,  )


# if b+c < 60 and b==0:
#     print(a, b+c)
# elif b+c >= 60:
#     a = a + (b+c)//60
#     b = (b+c)-60
#     print(a,b)
#     if a==23 :
#         a= 0 + (b+c)//60
#         b = (b+c)-60
#         print(a,b)
    

# 현재 시간에서 +m 만큼 ++
# m+c가 60을 안넘으면 h,m+c
# m+c가 60보다 크면 h+1, (m+c)-60
# 근데 h가 ==23이다 그러면 h는 0이되어야하는데 여기서 m+c가 // 1이면 0