def solution(s):
    answer = ""
    dic={'zero':'0','one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}
    i=0
    while i<len(s):
        if s[i]>='0' and s[i]<='9': answer+=s[i]
        else:
            tmp=""
            for j in range(i,len(s)):
                if s[j]<'0' or s[j]>'9': tmp+=s[j]
                try:
                    answer+=dic[tmp]
                    i=j
                    break
                except:
                    continue
        i+=1
    return int(answer)
