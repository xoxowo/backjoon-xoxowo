h,m = map(int, input().split())
c = int(input())



if m+c < 60:
    print(h, m+c)
elif h == 23 and m+c >= 60:
    m = (m+c)-60
    h = ((m+c)//60)
    print(h, m)

else :
    print(h+1,  )

    

# 현재 시간에서 +m 만큼 ++
# m+c가 60을 안넘으면 h,m+c
# m+c가 60보다 크고 120보다 작으면 h+1, (m+c)-60
# 근데 h가 ==23이다 그러면 h는 0이되어야하는데 여기서 m+c가 // 1이면 0