import sys
sys.stdin = open('input.txt')


def hoare_partition(left, right):
    # 피봇을 제일 왼쪽 값으로 지정, 시작점과 끝점 지정
    pivot = num_lst[left]
    start = left + 1
    end = right

    # 시작점이 끝점보다 커질 때까지 반복
    while start <= end:
        # 시작점의 수가 피봇보다 커질 때까지 시작점을 증가
        while start <= end and num_lst[start] <= pivot:
            start += 1

        # 끝점의 수가 피봇보다 작아질 때까지 끝점을 감소
        while start <= end and num_lst[end] >= pivot:
            end -= 1

        # 찾은 시작점이 찾은 끝점보다 작다면 둘의 자리를 교환
        if start < end:
            num_lst[start], num_lst[end] = num_lst[end], num_lst[start]

    # 반복 이후 피봇과 끝점의 자리를 교환 후 끝점 반환
    num_lst[left], num_lst[end] = num_lst[end], num_lst[left]
    return end


def quick_sort(left, right):
    # 왼쪽이 오른쪽보다 작다면 hoare 함수로 피봇을 찾은 후 왼쪽 범위 찾고 오른쪽 범위 찾기
    if left < right:
        pivot = hoare_partition(left, right)
        quick_sort(left, pivot - 1)
        quick_sort(pivot + 1, right)


T = int(input())
for tc in range(1, T+1):
    num_lst = list(map(int, input().split()))  # 정렬할 데이터
    quick_sort(0, len(num_lst)-1)  # 퀵 정렬 함수 호출
    print(f'#{tc}', *num_lst)  # 정렬된 데이터 출력