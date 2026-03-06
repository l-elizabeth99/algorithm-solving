import sys
sys.stdin = open('5207_input.txt')


def binary_search(target):
    left = 0  # 시작점
    right = len(A) - 1  # 끝점
    dir = ''  # 방향 종류
    find = False  # 못 찾았다고 가정

    # 시작점과 끝점이 교차될 때까지 반복
    while left <= right:
        # 중간점
        mid = (left + right) // 2

        # A의 중간점이 찾는 수라면 성공과 방향을 반환
        if A[mid] == target:
            return True, dir

        # target이 작은 경우
        # 방향이 오른쪽이거나 처음이라면 방향에 L을 넣고, 아니면 실패와 방향을 반환 후 끝점 재설정
        if target < A[mid]:
            if dir == 'R' or dir == '':
                dir = 'L'
            else:
                return False, dir
            right = mid - 1

        # target이 큰 경우
        # 방향이 왼쪽이거나 처음이라면 방향에 R을 넣고, 아니면 실패와 방향을 반환 후 시작점 재설정
        if target > A[mid]:
            if dir == 'L' or dir == '':
                dir = 'R'
            else:
                return False, dir
            left = mid + 1

    # 못 찾았다면 실패와 방향을 반환
    return find, dir


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())  # A의 정수 개수, B의 정수 개수
    A = sorted(map(int, input().split()))  # 입력받은 A를 정렬
    B = sorted(map(int, input().split()))  # 입력받은 B를 정렬

    # B를 돌며 함수에서 반환한 성공여부와 방향을 받고, 성공했다면 경우의 수 세기
    cnt = 0
    for b in B:
        is_found, direction = binary_search(b)
        if is_found:
            cnt += 1

    # 경우의 수 출력
    print(f'#{tc}', cnt)