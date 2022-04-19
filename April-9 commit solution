import sys
n=int(input())
building=list(map(int,input().split()))
result=0
for i in range(0,len(building)):
    tmp,ltmp,rtmp=0,sys.maxsize,-sys.maxsize+1
    for j in range(1,i+1):
        if min(((building[i]-building[i-j])/(j)),ltmp)!=ltmp or j==1:
            tmp+=1
            ltmp=min(((building[i]-building[i-j])/(j)),ltmp)
    for j in range(i+1,len(building)):
        if max(((building[j]-building[i])/(j-i)),rtmp)!=rtmp or j==i+1:
            tmp+=1
            rtmp=max(((building[ j ]-building[i])/(j-i)),rtmp)
    result=max(result,tmp)
print(result)
