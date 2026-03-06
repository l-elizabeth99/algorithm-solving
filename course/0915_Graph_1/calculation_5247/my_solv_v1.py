import sys
sys.stdin = open('sample_input.txt')

from collections import deque


def bfs(before_num, after_num):
    # 큐 생성 - 시작점(이전 숫자와 cnt)을 튜플로 묶어 큐에 넣고 시작
    # 이전 숫자의 방문 표시
    q = deque([(before_num, 0)])
    visited[before_num] = 1

    # 큐가 빌 때까지 반복
    while q:
        # 큐에서 뺀 값을 현재 수와 cnt로 지정
        curr_num, cnt = q.popleft()

        # 종료 조건: 현재 수가 만들어야 할 수와 같다면 cnt를 반환 후 종료
        if curr_num == after_num:
            return cnt

        # 사용 가능한 연산을 리스트로 생성
        possible_cal = [curr_num+1, curr_num-1, curr_num*2, curr_num-10]

        # 사용 가능한 연산만큼 다음 수를 만들고
        # 다음 수가 유효한 범위 내에 있고, 방문하지 않은 수라면 방문 처리 후 cnt+1과 함께 큐에 넣기
        for next_num in possible_cal:
            if 1 <= next_num <= 1000000 and visited[next_num] == 0:
                visited[next_num] = 1
                q.append((next_num, cnt+1))


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())  # 원 자연수, 만들어야 할 자연수
    visited = [0] * 1000001  # 가능한 최대 숫자의 사용 여부 기록
    result = bfs(N, M)  # 함수 호출

    # 결과 출력
    print(f'#{tc}', result)