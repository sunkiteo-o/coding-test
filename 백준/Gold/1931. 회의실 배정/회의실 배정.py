n = int(input())

timeArr = [list(map(int,input().split())) for _ in range(n)]
timeArr.sort(key=lambda x: (x[1],x[0]))

time = timeArr[0][1]
count = 1

for i in range(1,n):
    if time <= timeArr[i][0]:
        count+=1
        time = timeArr[i][1]
    else: 
        continue


print(count)