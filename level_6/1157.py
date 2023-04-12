"""
알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 
단, 대문자와 소문자를 구분하지 않는다.

입력
첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 
주어지는 단어의 길이는 1,000,000을 넘지 않는다.

출력
첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 
단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.

예제 입력           예제 출력
Mississipi          ?

zZa                 Z

z                   Z

"""

# n = input().upper() # 입력받은 알파벳 대문자로 변환하여 변수에 저장
# print(n)


# for _ in range(len(n)):
    
    
# if 

word = input().upper() # 입력받은 문자열을 대문자로 바꾼다.
counts = [0] * 26      # 알파벳을 카운트할 리스트를 만든다.

for c in word:
    if c.isalpha():   # 알파벳이면
        counts[ord(c) - ord('A')] += 1  # 해당 알파벳의 카운트를 1 증가시킨다.

max_count = max(counts)  # 가장 많이 나온 알파벳의 카운트를 구한다.
if counts.count(max_count) > 1:  # 최대 카운트를 가진 알파벳이 여러 개인 경우
    print("?")
else:  # 최대 카운트를 가진 알파벳이 하나인 경우
    print(chr(counts.index(max_count) + ord('A')))
