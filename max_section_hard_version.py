"""
저는 아래와 같은 방식으로 풀이를 사용하였습니다.
먼저 입력크기가 n일때 left와 right에 n만큼 0을 넣어줍니다.
입력으로 받은 리스트를 nums라고 합시다.
left에 담길 것은 자신의 왼쪽 인덱스에 있는 최대합의 값을 담습니다.
right는 자신의 오른쪽에 있는 최대합을 담습니다.
단, 자기 자신은 일단 합에서 제외시키는 것으로 합시다.
가독성을 위해 아래의 점화식을 첨부합니다.
left[i]=max(max(left[i-1],0)+nums[i-1],0)
right[i]=max(max(right[i+1],0)+nums[i+1],0)
위와 같이 하면 left의 경우 자신의 왼쪽 구간에서 최대합을 저장할 수 있고
right의 경우 오른쪽의 최대합을 저장하되 아직 자신은 합에 포함시키지 않은 상태입니다.
단, left[0]의 경우 0으로 유지시키고, right[0]의 경우도 0으로 유지시켰는데요,
그 이유는 left[0]은 왼쪽이 없고 right[0]은 오른쪽이 없기 때문입니다.
자기 자신을 제외시키는 이유는 합산하면서 자기 자신이 중복되어 더해지는 경우를 방지하기 위해섭니다.
결론적으로, 결과 result는
result[i]=left[i]+right[i]+nums[i]가 됩니다.
시간복잡도는 O(n)입니다.
"""
nums=list(map(int,input().split())) #입력
left,right=[0]*len(nums),[0]*len(nums) #각 배열 선언
for i in range(1,len(nums)):left[i]=max(max(left[i-1],0)+nums[i-1],0) #점화식의 규칙으로 값 갱신
for i in range(len(nums)-2,-1,-1):right[i]=max(max(right[i+1],0)+nums[i+1],0)#점화식의 규칙으로 값 갱신
for i in range(len(nums)): print(left[i]+right[i]+nums[i],end=" ") #결과 도출 및 출력
print()#줄바꿈이 필요
