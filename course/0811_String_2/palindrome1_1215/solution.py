# 목적 : 길이 x의 회문 개수 구하기
# 주어진 판에서 가로, 세로를 판별
# 가로, 세로 각각 길이가 x인 경우 찾아서 회문인지 확인
import sys
sys.stdin = open('input.txt')

'''
가로와 세로의 단어들 중에서
길이가 x인 단어를 찾고
그 단어가 회문인지 판단한 후
회문이라면 +1
모든 단어에 대한 판별이 끝나면
회문의 개수를 출력
'''


def is_palindrome(word):
    for i in range(len(word) // 2):  # 절반의 반복을 도는 동안
        if word[i] != word[len(word)-1-i]:  # 하나라도 다르면 회문이 아님
            return False
    return True  # 모든 반복을 정상적으로 돌았다면 회문임


T = 10
N = 8  # 주어진 판의 크기
for tc in range(1, T+1):
    L = int(input())  # 회문의 길이
    arr = [input() for _ in range(N)]
    result = 0

    # 가로(열 우선 탐색)의 문자열 찾기 (길이가 L인 문자열)
    for row in range(N):
        for col in range(N-L+1):
            word = []  # '' + '' 은 속도가 느림 -> list에 넣어 판단
            for delta in range(L):
                word.append(arr[row][col+delta])  # 글자의 처음 시작 위치
            # word가 회문인지 판별
            if is_palindrome(word):
                result += 1  # 회문 1 더함

    # 세로(행 우선 탐색)의 문자열 찾기 (길이가 L인 문자열)
    for col in range(N):
        for row in range(N-L+1):
            word = []  # '' + '' 은 속도가 느림 -> list에 넣어 판단
            for delta in range(L):
                word.append(arr[row+delta][col])  # 글자의 처음 시작 위치
            # word가 회문인지 판별
            if is_palindrome(word):
                result += 1  # 회문 1 더함

    print(f'#{tc}', result)