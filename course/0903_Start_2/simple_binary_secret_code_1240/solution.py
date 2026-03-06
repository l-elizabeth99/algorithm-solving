import sys
sys.stdin =open('input.txt')

'''
1. 암호코드 확보
    우측의 비트가 1 -> 문자열을 뒤에서부터 체크
    
'''
def scanner(code):
    for i in range(8):
        print(code[i+7])


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    barcode = set()
    for _ in range(N):
        code = input().rstrip('0')[-56:]
        if code and code not in barcode:
            scanner(code)
            barcode.add(code)

    print(barcode)