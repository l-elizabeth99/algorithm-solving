import sys
sys.stdin = open('input.txt')

'''
1
1 1 
1 2 1
1 3 3 1
1 4 6 4 1
1 5 10 10 5 1
1 6 15 20 15 6 1
1 7 21 35 35 21 7 1
1 8 29 56 70 56 29 8 1
1 9 37 85 126 126 85 37 9 1
1 10 46 122 211 252 211 122 46 10 1
1 11 56 168 333 463 463 333 168 56 11 1
1 12 67 224 501 796 926 796 501 224 67 12 1
'''

'''
첫 번째 줄은 1
두 번째 줄은 1 1
세 번째 줄은 1 2 1 - 2 : 이전 줄의 0과 1을 더한 것
네 번째 줄은 1 3(이전 줄의 0 + 1) 3(이전 줄의 (1 + 2) 1

# col의 0번 인덱스와 마지막 인덱스는 무조건 1
# 
# 반복 range(N)
#     [0] = 1
#     반복 i in range(연산의 횟수 = 이전 줄의 길이 - 1)
#         [중간 인덱스] = 더하기 연산 (i, i+1)
#     [-1] = 1
#     
#     이전 리스트 = 방금 만든 리스트
'''

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    # 이전 리스트
    before_lst = [1]

    # 반복 range(N)
    print(f'#{tc}')
    for _ in range(N):
        # [0] = 1
        temp_lst = [1]
        # 반복 i in range(연산의 횟수 = 이전 줄의 길이 - 1)
        for i in range(len(before_lst) - 1):
            # [중간 인덱스] = 더하기 연산 (i, i+1)
            temp = before_lst[i] + before_lst[i+1]
            temp_lst.append(temp)
        # [-1] = 1
        temp_lst.append(1)
        print(*before_lst)

        # 이전 리스트 = 방금 만든 리스트
        before_lst = temp_lst