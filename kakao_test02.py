def solution(places):
    answer = []
    for room in places:
        adhere=True
        for i in range(4):
            for j in range(5):
                if room[i][j]=='P':
                    if i<=2:
                        if room[i+2][j]=='P' and room[i+1][j]!='X':
                            adhere=False
                            break
                    if j==0:
                        if room[i+1][j]=='P' or room[i][j+1]=='P':
                            adhere=False
                            break
                        #대각선 규칙
                        if room[i+1][j+1]=='P' and (room[i+1][j]!='X'or room[i][j+1]!='X'):
                            adhere=False
                            break
                        if room[i][j+2]=='P' and room[i][j+1]!='X':
                            adhere=False
                            break
                    elif j<4:
                        if j<=2 and (room[i][j+2]=='P' and room[i][j+1]!='X'):
                            adhere=False
                            break
                        if room[i+1][j]=='P' or room[i][j+1]=='P':
                            adhere=False
                            break
                        #대각선 규칙
                        if room[i+1][j+1]=='P' and (room[i+1][j]!='X'or room[i][j+1]!='X'):
                            adhere=False #오른쪽 대각선
                            break
                        if room[i+1][j-1]=='P' and (room[i][j-1]!='X' or room[i+1][j]!='X'):
                            adhere=False
                            break
                    else:
                        if room[i][j-1]=='P' or room[i+1][j]=='P':
                            adhere=False
                            break
                        if room[i+1][j-1]=='P' and (room[i][j-1]!='X' or room[i+1][j]!='X'):
                            adhere=False
                            break
                if adhere==False: break
            if adhere==False:
                answer.append(0)
                break
        if adhere==True:answer.append(1)
        for i in range(4):
            if room[4][i]=='P' and room[4][i+1]=='P':
                answer[-1]=0
                break
    return answer
