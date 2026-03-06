import sys
sys.stdin = open('5202_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())  # 신청서 수
    working_times = []  # 작업 시간 정보를 담을 리스트

    for _ in range(N):
        s, e = map(int, input().split())  # 시작 시간, 종료 시간
        working_times.append((s, e))  # 시작 시간과 종료 시간을 작업 시간에 튜플로 묶어 넣기

    working_times.sort(key=lambda x: x[1])  # 종료 시간을 기준으로 오름차순으로 정렬
    count = 1  # 1로 초기화
    end_time = working_times[0][1]  # 종료 시간

    for i in range(1, N):  # 다음부터 끝까지 반복
        start_time = working_times[i][0]  # 시작 시간
        if start_time >= end_time:  # 시작 시간이 종료 시간 이상이면 카운트 증가, 종료 시간 갱신
            count += 1
            end_time = working_times[i][1]

    # 결과 출력
    print(f'#{tc}', count)