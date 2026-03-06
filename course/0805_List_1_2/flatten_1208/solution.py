import sys
sys.stdin = open('input.txt')

'''
* 평탄화 : 가장 높은 곳의 상자를 가장 낮은 곳으로 이동시키는 것
* 평탄화의 횟수 : 제한적
* 평탄화가 되었다 = 높낮이의 차이가 1이하
* 가로 길이 : 항상 100
* 상자 높이 : 1이상, 100 이하
* 목표 : 최고점 - 최저점
'''

T = 10  # 테스트 케이스 수
for tc in range(1, T+1):
    # 평탄화를 하려면 가장 높은 값과 가장 낮은 값을 찾아야 함
    # count list를 이용해 모든 높이를 확인 -> 최고점과 최저점 확인 -> 개수 세기
        # count list의 인덱스 : 건물의 높이
        # count list의 값 : 해당 높이의 개수
        # 최대 높이, 최소 높이 파악

    N = 100  # 상자의 개수
    L = int(input())  # 최대 덤프 횟수
    box_lst = list(map(int, input().split()))
    # print(L, box_lst)

    count_lst = [0] * (N+1)  # 박스의 높이가 1 이상 100 이하 / 인덱스 0을 제외하고 인덱스 100까지 가야함

    # 높이별로 개수 세기
    min_height = box_lst[0]
    max_height = box_lst[0]

    for i in range(N):
        heights = box_lst[i]
        count_lst[heights] += 1  # 박스 높이 세기

        # 최대 높이
        if heights > max_height:
            max_height = heights

        # 최소 높이
        if heights < min_height:
            min_height = heights

    # 한 번 덤프 시(지정된 횟수만큼 반복)
    for _ in range(L):
        # 더이상 평탄화할 것이 없다면
        if (max_height - min_height) <= 1:
            break

        # 최대 높이 개수 1 감소
        count_lst[max_height] -= 1  # 9층이 하나 감소하면
        count_lst[max_height-1] += 1  # 8층은 하나 증가

        # 최소 높이 개수 1 증가
        count_lst[min_height] -= 1  # 1층이 하나 감소하면
        count_lst[min_height+1] += 1  # 2층은 하나 증가

        # 최대/최소 높이가 하나도 존재하지 않으면
        # 다음 높이를 최대/최소로 갱신
        if count_lst[max_height] == 0:
            max_height -= 1  # 9층이 없다면 8층이 최대 높이

        if count_lst[min_height] == 0:
            min_height += 1  # 1층이 없다면 2층이 최소 높이

    print(f'#{tc}', max_height - min_height)