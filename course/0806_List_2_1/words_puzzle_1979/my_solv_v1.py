import sys
sys.stdin = open('input.txt')

T = int(input())  # 테스트 케이스 수

# 테스트 케이스를 순회하며 단어 퍼즐의 배열의 크기(N)와 단어의 길이(K) 받기
for tc in range(1, T+1):  # 테스트 케이스만큼 반복
    N, K = map(int, input().split())  # 단어 퍼즐의 배열의 크기(N)와 단어의 길이(K)

    # 5 <= N <= 15
    # 2 <= K <= N

    # 퍼즐의 모양은 2차원 정보 -> 2차원 배열로 저장
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 0은 검은색, 1은 흰색
    # 흰색 부분에 단어가 들어가야 함

    # 단어가 들어갈 자리의 수를 0으로 설정
    results = 0

    # 가로 방향 확인
    # 행 먼저 순회
    for i in range(N):
        counts = 0  # 연속된 흰색 부분의 수를 0으로 설정

        # 열 순회
        for j in range(N):
            if arr[i][j] == 1:  # 현재 칸이 1(흰색)이라면
                counts += 1  # 연속된 흰색 부분의 수를 갱신
            else:  # 현재 칸이 0(검은색)이라면
                if counts == K:  # 연속된 흰색 부분의 수가 단어의 수와 같다면
                    results += 1  # 단어가 들어갈 자리의 수를 갱신
                counts = 0  # 아니면 연속된 흰색 부분의 수를 0으로 갱신
        if counts == K:  # 연속된 흰색 부분의 수가 단어의 수와 같다면
            results += 1  # 단어가 들어갈 자리의 수를 갱신

    # 세로 방향 확인
    # 열 먼저 순회
    for j in range(N):
        counts = 0  # 연속된 흰색 부분의 수를 0으로 설정

        # 행 순회
        for i in range(N):
            if arr[i][j] == 1:  # 현재 칸이 1(흰색)이라면
                counts += 1  # 연속된 흰색 부분의 수를 갱신
            else:  # 현재 칸이 0(검은색)이라면
                if counts == K:  # 연속된 흰색 부분의 수가 단어의 수와 같다면
                    results += 1  # 단어가 들어갈 자리의 수를 갱신
                counts = 0  # 아니면 연속된 흰색 부분의 수를 0으로 갱신
        if counts == K:  # 연속된 흰색 부분의 수가 단어의 수와 같다면
            results += 1  # 단어가 들어갈 자리의 수를 갱신

    print(f'#{tc} {results}')  # 결과 출력