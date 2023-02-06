"""
두 자연수 A와 B가 있을 때, A % B는 A를 B로 나눈 나머지 이다.
예를 들어, 7, 14, 27, 38을 3으로 나눈 나머지는 1, 2, 0, 2이다. 

수 10개를 입력받은 뒤, 이를 42로 나눈 나머지를 구한다. 
그 다음 서로 다른 값이 몇 개 있는지 출력하는 프로그램을 작성하시오.

입력
첫째 줄부터 열번째 줄 까지 숫자가 한 줄에 하나씩 주어진다. 
이 숫자는 1,000보다 작거나 같고, 음이 아닌 정수이다.

출력
첫째 줄에, 42로 나누었을 때, 서로 다른 나머지가 몇 개 있는지 출력한다.
"""
list = []
s = []
for i in range(10):
    list.append(int(input()))

for i in range(10):
    if (list[i] % 42 == 0) == 0:
        s.append(list[i] % 42)
    else :
        s.append(list[i] % 42)
f = set(s)
#set함수는 중복을 제거해주는 대신 딕셔너리 값으로 변환
# f 프린트해보면 {, , , ,} 값으로 변환
print(len(f))
# 중복 값을 제거한 f의 길이를 출력하면 끝

"""
더 짧은 풀이
list = []
for i in range(10):
    n=int(input())
    list.append(n%42)

list = set(list)
print(len(list))

"""