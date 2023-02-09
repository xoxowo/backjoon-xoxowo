"""
어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다. 
등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다. 
N이 주어졌을 때, 1보다 크거나 같고, 
N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오. 

입력
첫째 줄에 1,000보다 작거나 같은 자연수 N이 주어진다.

출력
첫째 줄에 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력한다."""

# 한수가 뭐여.. 
# 각 항들이 일정한 차이를 보이는 수열 1,2,3 공차1 2,4,6 공차 2 이런..
# 결론은 1자리수 2자리수는 모두 한수.ㅋ...
# 그래서 99까지 한수다..ㅎ..
# 100부터 1000까지만 구하면된다...
# 예제 1에서 110을 넣었을 때 한수의 개수는 99이니 즉, 한수는 99개
# if (i <100) han = i;

a =int(input()) # 110
s=0
for i in range(1, a+1): 
    if i <= 99: # 결국 99까지는 한수이니 if문으로 s에 값추가
        s +=1
    else : # 100부터 리스트로 받아서 [100, 140, 180 ...] 리스트에 등차를 구한다.
        ss = list(map (int, str(i))) 
        if ss[0]-ss[1] == ss[1]-ss[2]: #등차가 같으면 s에 1추가해서 프린트하면 끝..
            s +=1
print(s)    