"""
dp테이블을 이용해 O(n^2)으로 해결하였습니다.
dp테이블을 완성할 때 두가지 조건에 직면하게 됩니다.
1. 매칭 조건이 맞는경우
2. 매칭 조건이 안맞는경우
1번의 경우 dp[i-1][j-1]+(발생한 골)과 dp[i-1][j] 그리고 dp[i][j-1] 중 가장 큰값을 dp[i][j]에 넣어줍니다.
그 이유는 대각선 위에 이전 조합들로의 최댓값이 저장되어져있고 dp테이블 상으로 
바로 위에 더 좋은 조합이 있을 수 있고 바로 왼쪽에 더 좋은 조합이 있을 수 있기 때문입니다.
2번의 경우 dp[i-1][j]와 dp[i][j-1]중 큰값을 넣어주는데요
조건에 맞지 않는 경우 0이 들어가는 것이 바람직해 보이지만, 그렇게 되는 경우 이전 조합에 대한 결과를
가져오는 과정에서 문제가 생겨 큰 값을 해당 자리에 넣어주면서 이전 조합을 가져올 수 있게 만들어줍니다.
2번에서 max함수에 넣는 요소 모두 1번에서 넣는 것이기에 중복되어 쓸데없이 코드가 길어지는 것을 막아주었습니다.
시간복잡도는 dp테이블 원소만큼 이중반복문을 돌리고 이중반복문 내에선 단순 비교나 갱신연산만 해주기에
O(n^2)입니다.
"""
def solve(kor, jpn, k_goals, j_goals):
	n = len(kor) - 1
	dp = [[0]*(n+1) for _ in range(n+1)]
	for i in range(1, n+1):
		for j in range(1, n+1):
			dp[i][j]=max(dp[i-1][j],dp[i][j-1]) #조건에 맞던 맞지 않던 max에 파라미터로 넣어줘야 할 값. 여기를 (a)라고 하겠음
			if kor[i]!=jpn[j] and (kor[i]=='W' and k_goals[i]>j_goals[j] or jpn[j]=='W' and k_goals[i]<j_goals[j]): #조건에 맞는경우만 갱신.
				dp[i][j]= max(k_goals[i]+j_goals[j]+dp[i-1][j-1],dp[i][j]) #현재 발생한 골과 이전 조합을 더한것과 (a)중 최댓값을 비교
	return dp[n][n]
#입력조건
kor = ' '+input()
k_goals = [0] + list(map(int,input().split()))
jpn = ' '+input()
j_goals = [0] + list(map(int,input().split()))
print(solve(kor, jpn, k_goals, j_goals))
