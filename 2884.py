h,m = map(int, input().split())

# 미리 알람 맞추기
# 현재 시간에서 45분 빼기
# 만약 현재 시간이 45분과같거나 크면 분에서 -45 빼면됨
# 만약 현재 시간 분이 45분 보다 작으면 시간 -1 분 -45 해야함
# 
if m >= 45:
    print(h, m-45)
elif h > 0 and m < 45:
    print(h-1, m+15)
else:
    print(23, m+15)