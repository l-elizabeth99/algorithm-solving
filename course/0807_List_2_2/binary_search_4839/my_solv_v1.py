import sys
sys.stdin = open('sample_input.txt')

# 이중 탐색 함수 선언(찾을 쪽 수, 전체 쪽 수 입력 받기)
def binary_search(find_page, total_page):
    count = 0  # 탐색 수를 0을 지정
    l = 1  # 왼쪽 첫번째 구간의 시작을 1로 지정
    r = total_page  # 오른쪽 첫번째 구간의 시작을 전체 쪽 수로 지정

    while l <= r:  # 왼쪽 구간이 오른쪽 구간보다 작거나 같을 때까지 반복
        count += 1  # 한 번 반복할 때마다 수 세기
        c = int((l + r) / 2)  # 중간값을 정수로 지정

        if c > find_page:  # 중간값이 찾을 쪽 수보다 크다면
            r = c  # 오른쪽 끝을 중간값으로 설정

        elif c < find_page:  # 중간값이 찾을 쪽 수보다 작다면
            l = c  # 왼쪽 끝을 중간값으로 설정

        else:  # 중간값이 찾을 쪽 수라면
            return count  # 탐색 수 반환

    return -1  # 못 찾으면 -1 반환


T = int(input())  # 테스트 케이스의 수

for tc in range(1, T+1):  # 테스트 케이스만큼 반복

    # 전체 쪽 수, a가 찾을 쪽 수, b가 찾을 쪽 수
    P, A, B = list(map(int, input().split()))

    # a와 b가 찾을 때까지 걸린 탐색 수 지정
    count_a = binary_search(A, P)
    count_b = binary_search(B, P)

    if count_a > count_b:  # a가 b가 크다면
        print(f'#{tc} B')  # b가 이김(B 출력)

    elif count_a < count_b:  # a가 b보다 작다면
        print(f'#{tc} A')  # a가 이김(A 출력)

    else:  # a와 b가 같다면
        print(f'#{tc} 0')  # 비김(0 출력)