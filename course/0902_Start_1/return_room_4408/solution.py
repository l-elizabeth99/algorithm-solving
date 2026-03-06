'''
학생이 본인 방으로 돌아가야 함

복도를 이용해 돌아가야 하는 경로가 중복되면 기다렸다가 가야 함

방 앞 복도의 사용횟수를 카운팅
중복되는 횟수의 복도는 기다린 횟수로 판단

복도의 사용횟수를 조사해 최소 단위 시간 판단 가능

방 앞의 복도 구별 필요
1, 2번방 => 0번 복도
3, 4번방 => 1번 복도

현재 방 번호에서 -1을 하고 나누기 2를 한 몫을 복도의 인덱스로
총 200개의 복도 필요

ex)
1->4 : 0, 1번 복도 사용
3->6 : 1, 2번 복도 사용
-> 1번 복도가 2번 사용 -> 최소 단위 시간 : 2
'''

import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())  # 돌아가야 할 학생 수
    corridors = [0] * 200  # 복도 리스트
    for _ in range(N):
        start_room, end_room = map(int, input().split())
        # 해당 방의 복도 계산
        start_corridor = (start_room - 1) // 2
        end_corridor = (end_room - 1) // 2

        # 큰 번호의 방에서 작은 번호의 방으로 가는 경우가 빠짐
        if start_corridor > end_corridor:
            start_corridor, end_corridor = end_corridor, start_corridor

        for i in range(start_corridor, end_corridor+1):  # 끝나는 방 앞의 복도까지 사용
            corridors[i] += 1
    # 모든 학생이 돌아갔다면 사용된 복도의 횟수가 corridors에 카운팅됨
    print(f'#{tc}', max(corridors))