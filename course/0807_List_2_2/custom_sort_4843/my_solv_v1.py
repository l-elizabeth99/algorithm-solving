import sys
sys.stdin = open('sample_input.txt')

'''
전 구간을 순회하며 오름차순으로 정렬

정수의 개수보다 하나 적게 반복
    최솟값을 첫번째 인덱스로 두기
    두번째부터 끝까지 반복
        현재 인덱스 값이 최소 인덱스 값보다 작으면
            최솟값을 현재 인덱스 값으로 갱신
    첫번째 인덱스와 최솟값의 인덱스 교환
    
새로 정렬된 리스트의 끝점과 시작점을 번갈아 넣기

새 리스트 생성

길이가 10이 될 때까지 반복
    원본 리스트의 (끝점, 시작점)을 새 리스트에 넣기
    원본 리스트의 끝점과 시작점을 갱신
'''

T = int(input())  # 테스트 케이스의 수

for tc in range(1, T+1):  # 테스트 케이스만큼 반복
    N = int(input())  # 정수의 개수
    a = list(map(int, input().split()))  # 정수 정보

    for i in range(N):  # 정수의 개수만큼 반복
        min_i = i  # 최솟값을 첫번째 인덱스로 지정

        for j in range(i+1, N):  # 두번째 인덱스부터 끝까지 반복
            if a[j] < a[min_i]:  # 현재 인덱스 값이 최솟값보다 작으면
                min_i = j  # 최솟값을 현재값으로 갱신

        a[i], a[min_i] = a[min_i], a[i]  # 첫번째와 최솟값의 정보 교환

    num = []  # 기준에 따라 정렬할 새 리스트 생성
    start = 0  # 시작점을 원본의 첫번째 인덱스로 지정
    end = N - 1  # 끝점을 원본의 마지막번째 인덱스로 지정

    while start <= end:  # 시작점이 끝점보다 작거나 같을 때까지 반복
        if start == 5:  # 시작점이 인덱스 5가 되면
            break  # 반복문 즉시 종료

        num.append(a[end])  # 끝점 추가
        num.append(a[start])  # 시작점 추가

        start += 1  # 시작점을 1 증가
        end -= 1  # 끝점을 1 감소

    print(f'#{tc}', *num)  # 결과 출력