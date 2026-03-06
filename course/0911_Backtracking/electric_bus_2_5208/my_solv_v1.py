import sys
sys.stdin = open('5208_input.txt')


def find_min_change(curr_pos, curr_cnt):
    global min_cnt

    # 가지치기: 현재 횟수가 최소 횟수 이상이면 종료
    if curr_cnt >= min_cnt:
        return

    # 종료 조건: 현재 위치가 종점이면 최소 횟수 갱신 후 종료
    if curr_pos >= N-1:
        if curr_cnt < min_cnt:
            min_cnt = curr_cnt
        return

    # 현재의 다음 위치부터 현재 배터리 용량으로 갈 수 있는 위치의 정류장까지를 순회
    for idx in range(1, M_lst[curr_pos]+1):
        # 다음 위치 지정 후 다음 정류장으로 재귀 호출
        next_pos = curr_pos + idx
        find_min_change(next_pos, curr_cnt+1)


T = int(input())
for tc in range(1, T+1):
    info = list(map(int, input().split()))  # 정류장 수, 배터리 용량을 담은 리스트
    N = info[0]  # 정류장 수
    M_lst = info[1:]  # 정류장 별 배터리 용량
    min_cnt = float('inf')  # 최소 교환 횟수 초기화
    find_min_change(0, -1)  # 함수 호출
    print(f'#{tc}', min_cnt)  # 최소 횟수 출력