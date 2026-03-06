import sys
sys.stdin = open('input1.txt')

T = int(input())  # 테스트 케이스 수
for tc in range(1, T+1):  # 테스트 케이스만큼 반복
    N, M = map(int, input().split())  # N줄, M개
    arr = [list(map(int, input().split())) for _ in range(N)]  # NxM 배열 정보

    '''
    최댓값을 0으로 지정
    
    방향별로 더할 값 지정
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    
    N만큼 반복 - 행 먼저 순회
        M만큼 반복 - 다음 열 순회
            현재 꽃가루 수를 arr[i][j]로 지정
            
            4번 반복 - 상하좌우 만큼 반복
                행과 열에 각각 더하기
                ni = i+di[k]
                nj = j+dj[k]
                
                ni와 nj가 범위 안에 있다면
                    현재 꽃가루 수를 갱신
                    arr[ni][nj]
                        
            현재 꽃가루 수가 최댓값보다 크다면
                최댓값을 현재 꽃가루 수로 갱신
                    
    결과값 출력
    '''

    max_pollen = 0  # 꽃가루의 최댓값을 0으로 지정

    # 방향별로 더할 값 지정
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    for i in range(N):  # 행 먼저 N만큼 반복
        for j in range(M):  # 열 M만큼 반복
            current_pollen = arr[i][j]  # 현재 꽃가루 수 지정

            for k in range(4):  # 4번 반복(상하좌우)

                # 행과 열에 각각 더하기
                ni = i + di[k]
                nj = j + dj[k]

                if 0 <= ni < N and 0 <= nj < M:  # 유효한 인덱스라면
                    current_pollen += arr[ni][nj]  # 현재 꽃가루 수를 갱신

            if current_pollen > max_pollen:  # 현재 꽃가루 수가 최댓값보다 크다면
                max_pollen = current_pollen  # 최대값을 현재 꽃가루 수로 갱신

    print(f'#{tc} {max_pollen}')  # 결과 출력