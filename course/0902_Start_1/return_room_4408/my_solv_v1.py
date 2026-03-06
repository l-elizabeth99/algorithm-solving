import sys
sys.stdin = open('sample_input.txt')

# 이동구간 체크를 위한 리스트 생성
# 학생 수만큼 반복
# before_num, after_num 받기
# 이동구간 체크 - (num+1)//2로 계산
# # 이동구간 = (before_num + 1) // 2 ~ (after_num + 1) // 2 만큼 리스트에 1씩 누적
# 리스트에서 최댓값 구하기
# 단위시간 = 최댓값

T = int(input())  # 테스트 케이스
for tc in range(1, T+1):  # 테스트 케이스 수
    N = int(input())  # 돌아가야 할 학생 수
    count = [0] * 201  # 이동구간 체크를 위한 리스트
    for _ in range(N):  # 학샐 수만큼 반복
        before_num, after_num = map(int, input().split())  # 현재 방 위치, 돌아가야 할 방 위치
        start = (before_num + 1) // 2  # 시작 방 번호
        end = (after_num + 1) // 2  # 마지막 방 번호
        if start > end:  # 시작 방 번호가 마지막 방 번호보다 크다면 둘이 교환
            start, end = end, start
        for num in range(start, end+1):  # 시작 방부터 마지막 방까지 반복
            count[num] += 1  # 해당 방의 이동구간 체크
    print(f'#{tc}', max(count))  # 결과 출력 - 최대 체크 수