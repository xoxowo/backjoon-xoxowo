"""
두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

첫째 줄에 테스트 케이스의 개수 T가 주어진다.
각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)
"""
t= int(input())
s= [list(map(int, input().split())) for _ in range(t)]

# 여러번 출력 필요없을 때 break 사용하기
for i in range(t):
    for j in s:
        print(j[0]+j[1])
    break
