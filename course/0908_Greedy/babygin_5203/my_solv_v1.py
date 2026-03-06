import sys
sys.stdin = open('5203_input.txt')


def babygin(cards):
  count = [0] * 10  # 0~9까지의 개수를 담을 리스트

  # 카드를 순회하며 리스트에 해당 카드의 수를 누적
  for card in cards:
    count[card] += 1

  # 카드의 종류(10개)만큼 반복
  for i in range(10):
    # 현재 카드의 개수가 3 이상이면 T
    if count[i] >= 3:
      return True

    # 현재 숫자가 7 이하고, 해당 카드의 수가 1 이상이고, 다음 카드의 수가 1 이상이고, 그 다음 카드의 수가 1이상이면 T
    if i <= 7 and count[i] >= 1 and count[i+1] >= 1 and count[i+2] >= 1:
      return True

  # 그외에는 F
  return False


T = int(input())
for tc in range(1, T+1):
  num_list = list(map(int, input().split()))  # 숫자 정보

  # 승자, 각 플레이어의 카드를 지정
  winner = 0
  player_1_cards = []
  player_2_cards = []

  # 카드의 개수(12개)만큼 반복
  for i in range(12):
    # 해당 인덱스가 짝수면 플레이어 1의 카드에 현재 카드 넣기
    if i % 2 == 0:
      player_1_cards.append(num_list[i])

      # 카드의 수가 3개 이상인 경우
      if len(player_1_cards) >= 3:
        # 카드를 오름차순으로 정렬한 것을 파라미터로 두고 함수 호출
        # 호출결과가 있으면 플레이어 1이 승자
        if babygin(sorted(player_1_cards)):
          winner = 1
          break
    else:
      # 해당 인덱스가 홀수면 플레이어 2의 카드에 현재 카드 넣기
      player_2_cards.append(num_list[i])

      # 카드의 수가 3개 이상인 경우
      if len(player_2_cards) >= 3:
        # 카드를 오름차순으로 정렬한 것을 파라미터로 두고 함수 호출
        # 호출결과가 있으면 플레이어 2가 승자
        if babygin(sorted(player_2_cards)):
          winner = 2
          break

  # 숭자 출력
  print(f'#{tc}', winner)