# [Silver II] 섬의 개수 - 4963 

[문제 링크](https://www.acmicpc.net/problem/4963) 

### 성능 요약

메모리: 114940 KB, 시간: 160 ms

### 분류

그래프 이론, 그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색, 격자 그래프, 플러드 필

### 제출 일자

2025년 12월 9일 23:14:12

## 리뷰 

처음에 시간 초과가 나서 `input()`  을 `readline()`  으로 변경해줬더니 그래도 여전했다. 

구글링 해보니까 이 문제는 **pypy3**으로 돌려야 한대서 바꿔서 제출하니까 다음은 **메모리 초과**가 났다.

원인은 큐에 중복된 값이 들어가는 게 문제였다. 

조건 처리 밑에서 visited 배열을 True로 변경해줘야 다음 탐색 때 중복된 값을 안 넣을 수 있다.

```cpp
    while q:
        cy, cx = q.popleft()
        

        # 상하좌우, 대각선 탐색
        for dy,dx in dist:
            ny = cy+dy
            nx = cx+dx

            if 0<=ny<h and 0<=nx<w and not visited[ny][nx] and arr[ny][nx]==1:
                visited[ny][nx] = True <<여기를 넣어줘야함
                q.append([ny,nx])
```

