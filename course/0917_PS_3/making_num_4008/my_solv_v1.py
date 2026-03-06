import sys
sys.stdin = open('sample_input.txt')


def calculation(cnt, total, plus_cnt, minus_cnt, times_cnt, divide_cnt):
    global max_value, min_value

    # cnt가 끝까지 오면 최솟값과 최댓값 갱신 후 종료
    if cnt == N:
        min_value = min(min_value, total)
        max_value = max(max_value, total)
        return

    # 해당 연산자가 남아있다면 결과에 해당 연산을 계산하고 해당 연산 개수를 줄이기
    if plus_cnt > 0:
        calculation(cnt+1, total+num_lst[cnt], plus_cnt-1, minus_cnt, times_cnt, divide_cnt)

    if minus_cnt > 0:
        calculation(cnt+1, total-num_lst[cnt], plus_cnt, minus_cnt-1, times_cnt, divide_cnt)

    if times_cnt > 0:
        calculation(cnt+1, total*num_lst[cnt], plus_cnt, minus_cnt, times_cnt-1, divide_cnt)

    if divide_cnt > 0:
        calculation(cnt+1, int(total/num_lst[cnt]), plus_cnt, minus_cnt, times_cnt, divide_cnt-1)


T = int(input())
for tc in range(1, T+1):
    N = int(input())  # 숫자 개수
    operation_cnt_lst = list(map(int, input().split()))  # 각 연산자별 개수
    num_lst = list(map(int, input().split()))  # 수식에 들어갈 숫자

    # 최댓값, 최솟값 초기화
    max_value = float('-inf')
    min_value = float('inf')

    # 함수 호출 후 결과 계산 및 출력
    calculation(1, num_lst[0], operation_cnt_lst[0], operation_cnt_lst[1], operation_cnt_lst[2], operation_cnt_lst[3])
    result = max_value - min_value
    print(f'#{tc}', result)