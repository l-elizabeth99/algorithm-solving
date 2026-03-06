import sys
sys.stdin = open('5204_input.txt')


def merge(left_lst, right_lst):
    global cnt

    # 병합 과정에서 왼쪽 마지막 값이 오른쪽 마지막 값보다 크다면 cnt 1 증가
    if left_lst[-1] > right_lst[-1]:
        cnt += 1

    # 양쪽을 병합한 결과 리스트 생성
    result = [0] * (len(left_lst) + len(right_lst))
    left = right = 0

    # 두 리스트에서 비교할 대상이 없을 때 까지 반복
    while left < len(left_lst) and right < len(right_lst):
        # 왼쪽 값이 오른쪽 값보다 작다면 둘을 더한 위치의 결과값을 왼쪽값으로 지정
        if left_lst[left] < right_lst[right]:
            result[left + right] = left_lst[left]
            left += 1
        # 왼쪽 값이 오른쪽 값보다 크다면 둘을 더한 위치의 결과값을 오른쪽값으로 지정
        else:
            result[left + right] = right_lst[right]
            right += 1

    # 왼쪽 리스트에 남은 데이터들을 결과에 추가
    while left < len(left_lst):
        result[left + right] = left_lst[left]
        left += 1

    # 오른쪽 리스트에 남은 데이터들을 결과에 추가
    while right < len(right_lst):
        result[left + right] = right_lst[right]
        right += 1

    return result


def merge_sort(lst):
    # 종료 조건 : 리스트의 길이가 1이 되면 리스트 반환
    if len(lst) == 1:
        return lst

    # 절반 씩 나누어 분할
    mid = len(lst) // 2  # 리스트의 중간
    left = lst[:mid]     # 리스트의 왼쪽 절반
    right = lst[mid:]    # 리스트의 오른쪽 절반

    # 왼쪽 리스트, 오른쪽 리스트를 재귀로 설정
    left_lst = merge_sort(left)
    right_lst = merge_sort(right)

    # 분할이 완료되면 병합
    merged_list = merge(left_lst, right_lst)
    return merged_list


T = int(input())
for tc in range(1, T+1):
    N = int(input())  # 정수 개수
    A_lst = list(map(int, input().split()))  # N개의 정수
    cnt = 0  # 경우의 수 초기화
    sorted_A = merge_sort(A_lst)  # 함수 호출
    print(f'#{tc}', sorted_A[N//2], cnt)  # 결과 출력