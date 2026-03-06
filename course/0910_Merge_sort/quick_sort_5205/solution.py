import sys
sys.stdin = open('5205_input.txt')

'''
퀵 소트 구현 후 N//2 요소 출력

퀵 소트란
pivot을 정해서
pivot을 기준으로 작은 건 왼쪽으로, 큰 건 오른쪽으로 지정 후 다시 퀵 소트를 진행
'''


# def quick_sort(arr, left, right):
#     if left < right:
#         mid = partition(arr, left, right)
#         quick_sort(arr, left, mid-1)  # 작은 쪽 정렬
#         quick_sort(arr, mid+1, right)  # 큰 쪽 정렬
#     return arr
#
#
# def partition(arr, left, right):
#     # pivot은 왼쪽 첫번째 요소
#     pivot = arr[left]
#
#     # 왼쪽에서 오른쪽으로 이동하며 pivot보다 큰 요소를 찾는 인덱스 변수
#     i = left + 1
#
#     # 오른쪽에서 왼쪽으로 이동하며 pivot보다 작은 요소를 찾는 인덱스 변수
#     j = right
#
#     while i <= j:  # i가 j이하면 계속 탐색
#         while i <= j:
#             if pivot < arr[i]:  # pivot보다 큰 값을 찾으면 종료
#                 break
#             i += 1
#
#         while i <= j:
#             if pivot > arr[j]:  # pivot보다 작은 값을 찾으면 종료
#                 break
#             j -= 1
#
#         # while의 조건으로 인해 반복이 종료된 경우에는 i, j의 위치를 바꾸면 안됨
#         if i < j:
#             arr[i], arr[j] = arr[j], arr[i]
#
#     # i, j의 교차이후 j, pivot 위치 교환
#     # pivot을 기준으로, 큰 값은 i번째부터 시작, 작은 값은 j번까지 위치
#     # 작은 값에서의 마지막 요소와 pivot의 위치를 변경하면 pivot을 기준으로 정렬됨
#     arr[left], arr[j] = arr[j], arr[left]
#     return j  # 현재 pivot의 위치


# python 리스트의 가변성을 활용한 quick sort
def quick_sort(num_list):
    # base case
    # 요소가 하나만 있으면 종료
    if len(num_list) <= 1:
        return num_list

    pivot = num_list[0]  # 기준점은 가장 왼쪽 값으로 설정
    left = []
    right = []
    for idx in range(1, len(num_list)):
        if num_list[idx] < pivot:
            left.append(num_list[idx])
        else:
            right.append(num_list[idx])

    return [*quick_sort(left), pivot, *quick_sort(right)]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num_lst = list(map(int, input().split()))
    result = quick_sort(num_lst)
    print(f'#{tc}', result[N//2])