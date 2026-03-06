import sys
sys.stdin = open('input.txt')

T = int(input())  # 테스트 케이스 수

for tc in range(1, T+1):  # 테스트 케이스를 반복
    N = int(input())  # 숫자열 개수
    arr = list(map(int, input().split()))  # 숫자열 정보

    '''
    전 구간을 순회하며 가장 작은 값 찾기
    가장 작은 값과 첫번째 값의 위치 교환
    '''

    for i in range(N-1):  # 숫자열의 갯수보다 하나 작게 반복
        min_i = i  # 최솟값을 첫번째로 두기

        for j in range(i+1, N):  # 두번째부터 끝까지 순회
            if arr[j] < arr[min_i]:  # 현재값이 최솟값보다 작다면
                min_i = j  # 최솟값을 현재값으로 갱신

        arr[i], arr[min_i] = arr[min_i], arr[i]  # 최솟값과 첫번째값의 위치를 교환

    print(f'#{tc}', *arr)  # 결과를 출력(모든 요소를 하나씩 표기)